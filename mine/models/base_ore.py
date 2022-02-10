from django.db import models


class BaseOre(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Руда'

    mass = models.PositiveSmallIntegerField(verbose_name='Тонн руды')
    sio2 = models.FloatField(verbose_name='SiO2', default=0.0)
    fe = models.FloatField(verbose_name='Fe', default=0.0)
    
    def clean(self):
        if self.mass == 0:
            self.sio2 = 0
            self.fe = 0
