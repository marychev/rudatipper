from django.db import models


class Mine(models.Model):
    class Meta:
        verbose_name = 'Шахта'

    title = models.CharField(verbose_name='Наименование', max_length=256, default='Карьер шахта 001', unique=True)

    def __str__(self):
        return self.title
