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

    def calc_mass(self) -> int:
        return self.store.mass + self.cargo.mass

    def calc_characteristics(self) -> dict:
        sio2 = self.store.sio2 + self.cargo.sio2
        fe = self.store.fe + self.cargo.fe

        return {
            'sio2': sio2,
            'fe': fe
        }
