from django.db import models


class TModel(models.Model):
    class Meta:
        verbose_name = 'Модель самосвала'
        unique_together = ('title', 'code', 'max_mass')

    title = models.CharField(verbose_name='Наименование', max_length=256, default='БЕЛАЗ')
    code = models.CharField(verbose_name='Модель (код)', max_length=256, default='Б-22')
    max_mass = models.PositiveSmallIntegerField(verbose_name='Максимальная грузоподъемность (т.руды)', default=100)

    def __str__(self):
        return '{}: {}'.format(self.title, self.code)
