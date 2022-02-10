from django.db import models
from mine.models import Cargo
from store.models import Store


class History(models.Model):
    class Meta:
        verbose_name = 'История доставки на склад'
        verbose_name_plural = 'История доставки на склады'

    store = models.ForeignKey(Store, verbose_name='Склад', on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, verbose_name='Груз', on_delete=models.CASCADE)
    coordinates = models.CharField(
        verbose_name='Координаты разгрузки (x y)', max_length=8, blank=True, null=True,
        help_text="Format: x y / x, y / (x, y)")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.store, self.cargo, self.created)

    @property
    def parse_coordinates(self) -> tuple:
        return self.coordinates.split() if ' ' in self.coordinates else self.coordinates.split(', ')

    def can_ship_to_store(self) -> bool:
        return len(self.parse_coordinates) == 2 and not self.cargo.has_overload
