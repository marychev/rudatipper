from django.db import models
from tipper.models import TModel


class Tipper(models.Model):
    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'
        unique_together = ('number', 'tmodel')

    number = models.CharField(verbose_name='Бортовой номер', max_length=8, default='101')
    tmodel = models.ForeignKey(TModel, verbose_name='Модель', on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.number, self.tmodel)
