from django.core.exceptions import ValidationError
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
    max_mass = models.PositiveIntegerField(verbose_name='Макс. груз (т)', blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def to_tuple(cls, coordinates: str) -> tuple:
        coordinates = coordinates.split()
        if len(coordinates) == 2 and coordinates[0].isdigit() and coordinates[1].isdigit():
            coordinates = int(coordinates[0]), int(coordinates[1])
            return tuple(coordinates)
        return tuple()

    @property
    def parse_polygon(self) -> tuple:
        polygon = self.polygon.replace('((', '').replace('))', '').split(', ')
        return tuple([self.to_tuple(coordinates=c) for c in polygon])

    def clean(self):
        if len(self.parse_polygon) < 4:
            raise ValidationError('Неверный формат! Значения должны быть формата: ((30 10, 40 40, 20 40, 10 20, 30 10))')
