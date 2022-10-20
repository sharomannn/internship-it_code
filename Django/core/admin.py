from django.contrib import admin
from core import models

class ItemResultInline(admin.TabularInline):
    model = models.ItemResult

@admin.register(models.Item)
class Item(admin.ModelAdmin):
    inlines = (ItemResultInline, )
    list_display = ('name', 'done')
    list_filter = ('name',)

@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)



# @admin.register(models.Person)
# class Person(admin.ModelAdmin):
#     list_display = ('name', 'phone')
#     list_filter = ('name',)
#     pass