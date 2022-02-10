from django.db import models
from mine.models import BaseOre


class Store(BaseOre):
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    title = models.CharField(verbose_name='Наименование', default='Склад 42', unique=True, max_length=256)
    polygon = models.CharField(
        verbose_name="Полигон", max_length=512, default="((30 10, 40 40, 20 40, 10 20, 30 10))",
        help_text="Mask example: ((30 10, 40 40, 20 40, 10 20, 30 10))")
    max_mass = models.PositiveIntegerField(verbose_name='Макс. грузоподъемность (т)', blank=True, null=True)

    def __str__(self):
        return self.title
