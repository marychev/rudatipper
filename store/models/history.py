from django.core.exceptions import ValidationError
from django.db import models
from mine.models import Cargo
from store.models import Store


class History(models.Model):
    class Meta:
        verbose_name = 'История доставки на склад'
        verbose_name_plural = 'История доставки на склады'
        unique_together = ('store', 'cargo')

    store = models.ForeignKey(Store, verbose_name='Склад', on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, verbose_name='Груз', on_delete=models.CASCADE)
    coordinates = models.CharField(
        verbose_name='Координаты разгрузки (x y)', max_length=8, blank=True, null=True,
        help_text="Format: X Y")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.store, self.cargo, self.created)

    @property
    def parse_coordinates(self) -> tuple:
        return self.store.to_tuple(self.coordinates)

    @property
    def enter_to_polygon(self) -> bool:
        polygon = self.store.parse_polygon
        coordinates = self.parse_coordinates

        xs = [p[0] for p in polygon]
        ys = [p[1] for p in polygon]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        if len(coordinates) == 2 and min_x <= coordinates[0] <= max_x and min_y <= coordinates[1] <= max_y:
            return True
        return False

    @property
    def can_ship_to_store(self) -> bool:
        return self.enter_to_polygon

    def clean(self):
        if self.coordinates and len(self.parse_coordinates) != 2:
            raise ValidationError('Неверный формат! Значения должны быть формата: Х У')

    def calc_after_mass(self) -> int:
        return self.store.mass + self.cargo.mass

    @classmethod
    def percent_to_mass(cls, percent, mass):
        return percent * mass / 100

    @classmethod
    def mass_to_percent(cls, mass, after_mass):
        return round((mass * 100) / after_mass, 2)

    def calc(self) -> dict:
        # Масса хранилища и масса характеристик
        store_sio2_mass = self.percent_to_mass(self.store.sio2, self.store.mass)
        store_fe_mass = self.percent_to_mass(self.store.fe, self.store.mass)
        store_z_percent = 100 - float(self.store.sio2 + self.store.fe)
        store_z_mass = self.percent_to_mass(store_z_percent, self.store.mass)

        # Масса груза и масса характеристик
        cargo_sio2_mass = self.percent_to_mass(self.cargo.sio2, self.cargo.mass)
        cargo_fe_mass = self.percent_to_mass(self.cargo.fe, self.cargo.mass)
        cargo_z_percent = 100 - float(self.cargo.sio2 + self.cargo.fe)
        cargo_z_mass = self.percent_to_mass(cargo_z_percent, self.cargo.mass)

        # Общая масса груза и общая масса характеристик и процентного соотношения
        after_sio2_mass = store_sio2_mass + cargo_sio2_mass
        after_fe_mass = store_fe_mass + cargo_fe_mass
        after_mass = after_sio2_mass + after_fe_mass + (store_z_mass + cargo_z_mass)

        after_sio2_percent = self.mass_to_percent(after_sio2_mass, after_mass)
        after_fe_percent = self.mass_to_percent(after_fe_mass, after_mass)

        result = {
            'has_valid': self.enter_to_polygon,
            'error': '',
            'store': self.store,
            'before_mass': self.store.mass,
            'after_mass': self.store.mass,
            'before_characteristics': '{}% SiO2, {}% Fe'.format(self.store.sio2, self.store.fe),
            'after_characteristics': '{}% SiO2, {}% Fe'.format(
                after_sio2_percent,
                after_fe_percent
            ),
        }

        if self.enter_to_polygon:
            result.update({
                'after_mass': self.calc_after_mass()
            })
        else:
            result.update({
                'error': 'Не возможно отправить груз {} на склад {}.'.format(self.cargo, self.store.polygon)
            })

        return result
