from django.db import models
from mine.models import Mine, BaseOre
from tipper.models import Tipper


class Cargo(BaseOre):
    class Meta:
        verbose_name = 'Груз'

    mine = models.ForeignKey(Mine, verbose_name='Карьер/шахата', on_delete=models.CASCADE)
    tipper = models.ForeignKey(Tipper, verbose_name='Самосвал/шахата', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.mine)
