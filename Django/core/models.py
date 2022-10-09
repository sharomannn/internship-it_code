from django.db import models


class Person(models.Model):
    name = models.CharField('Name', max_length=255)
    phone = models.IntegerField('Number phone')
