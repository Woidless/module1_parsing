from django.db import models


class Hotel(models.Model):
    image = models.CharField('Картина', max_length=200, null=True)
    date =  models.CharField('Дата', max_length=100, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, null=True)
    currency = models.CharField('Валюта', max_length=100, null=True)


    def __str__(self) -> str:
        return 'Билеты' 

