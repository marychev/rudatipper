# Generated by Django 4.0.2 on 2022-02-09 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='БЕЛАЗ', max_length=256, verbose_name='Наименование')),
                ('code', models.CharField(default='Б-22', max_length=256, verbose_name='Модель (код)')),
                ('max_mass', models.PositiveSmallIntegerField(default=100, verbose_name='Максимальная грузоподъемность (т.руды)')),
            ],
            options={
                'verbose_name': 'Модель самосвала',
                'unique_together': {('title', 'code', 'max_mass')},
            },
        ),
        migrations.CreateModel(
            name='Tipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='101', max_length=8, verbose_name='Бортовой номер')),
                ('tmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipper.tmodel', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Самосвал',
                'unique_together': {('number', 'tmodel')},
            },
        ),
    ]
