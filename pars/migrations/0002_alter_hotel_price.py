# Generated by Django 4.1.6 on 2023-02-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
