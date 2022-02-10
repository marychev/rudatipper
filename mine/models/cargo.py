import math

from django.db import models
from mine.models import Mine, BaseOre
from tipper.models import Tipper


class Cargo(BaseOre):
    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

    mine = models.ForeignKey(Mine, verbose_name='Карьер/шахата', on_delete=models.CASCADE)
    tipper = models.ForeignKey(Tipper, verbose_name='Самосвал', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.mine)

    @property
    def has_overload(self) -> bool:
        if self.tipper and self.tipper.tmodel:
            return self.mass >= self.tipper.tmodel.max_mass
        return True

    @property
    def overload(self) -> float:
        if (self.tipper and self.tipper.tmodel) and (self.tipper.tmodel.max_mass - self.mass <= 0):
            diff = abs(self.tipper.tmodel.max_mass - self.mass)
            return round(diff * 100 / self.tipper.tmodel.max_mass, 2)
        return 0

    @property
    def max_mass(self) -> int:
        if self.tipper and self.tipper.tmodel:
            return self.tipper.tmodel.max_mass
        return 0
