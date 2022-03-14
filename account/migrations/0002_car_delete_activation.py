# Generated by Django 4.0.1 on 2022-01-30 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('color', models.CharField(choices=[('Bl', 'Black'), ('R', 'Red'), ('W', 'White'), ('B', 'Blue')], default='W', max_length=50, verbose_name='Цвет')),
                ('company', models.CharField(max_length=50, verbose_name='Компания')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(1800)], verbose_name='Год выпуска')),
                ('country', models.CharField(choices=[('K', 'Kaz'), ('R', 'Rus'), ('T', 'Tur'), ('G', 'Ger')], default='K', max_length=50, verbose_name='Страна выпуска')),
                ('owner', models.CharField(max_length=50, verbose_name='Владелец')),
                ('automatic_box', models.CharField(choices=[('R', 'Robot'), ('V', 'Variator')], max_length=50, null=True, verbose_name='Вид автомата коробки')),
                ('insurance_date', models.DateField(null=True, verbose_name='Дата страховки')),
                ('is_damaged', models.BooleanField(default=False, verbose_name='Повреждения')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
                'ordering': ('year',),
            },
        ),
        migrations.DeleteModel(
            name='Activation',
        ),
    ]