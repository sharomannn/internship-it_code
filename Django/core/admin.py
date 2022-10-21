from django.contrib import admin
from core import models


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ('name', 'done')
    list_filter = ('name',)

@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
