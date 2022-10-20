import datetime
from django.utils.timezone import  now
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
class Item(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255, blank=True, default='', unique=True)
    description = models.TextField(' Oписание', help_text='Подсказка для понимания', blank=True)
    priority = models.IntegerField('Приоритет сортировки', default=1, db_index=True)
    done = models.DateTimeField('Выполнено', null=True, blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True, db_index=True)
    updated = models.DateTimeField('Обновлён', auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', blank=True, related_name='items')

    class Meta:
        verbose_name = 'Дела'
        verbose_name_plural = 'Список дел'
        ordering = ('priority', 'created')

    def __str__(self):
        return self.name

    def duration(self) -> datetime.timedelta:
        return now() - self.created

class ItemResult(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    image = models.ImageField()

class Person(models.Model):
    name = models.CharField('Name', max_length=255)
    phone = models.IntegerField('Number phone')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name

