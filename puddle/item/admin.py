from django.contrib import admin

from .models import Category,Item
#registrando a tabela no banco de dados
admin.site.register(Category)
admin.site.register(Item)
