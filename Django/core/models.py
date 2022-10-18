from django.db import models


class Person(models.Model):
    name = models.CharField('Name', max_length=255)
    phone = models.IntegerField('Number phone')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name

