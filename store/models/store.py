from django.db import models
from mine.models import BaseOre


class Store(BaseOre):
    class Meta:
        verbose_name = 'Склад'

    title = models.CharField(verbose_name='Наименование', default='Склад 42', unique=True, max_length=256)
    polygon = models.CharField(
        verbose_name="Полигон", help_text="Mask example: ((4, 4), (4, 6), (6, 6), (6, 4), (4, 4))", max_length=512)
    max_mass = models.PositiveIntegerField(verbose_name='Максимально (т.)', blank=True, null=True)

    def __str__(self):
        return self.title
