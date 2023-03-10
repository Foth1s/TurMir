# Generated by Django 4.1.2 on 2022-10-21 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('place', models.TextField(verbose_name='Место')),
                ('date', models.DateField(verbose_name='Дата')),
                ('type_tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tourtype', verbose_name='Тип тура')),
            ],
        ),
    ]
