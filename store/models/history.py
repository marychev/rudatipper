from django.db import models
from mine.models import Cargo
from store.models import Store


class History(models.Model):
    class Meta:
        verbose_name = 'История доставки на склад'

    store = models.ForeignKey(Store, verbose_name='Склад', on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, verbose_name='Груз', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.store, self.cargo, self.created)
