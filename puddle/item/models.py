from django.db import models
from django.contrib.auth.models import User
#criando um modelo de banco de dados
class Category(models.Model):
    name=models.CharField(max_length=255)
    #correção da apresentação das tabelas no django admin
    class Meta:
        #organizando as categorias por nomes
        ordering=('name',)
        verbose_name_plural='Categories'
    #apresentação dos nomes das categorias na tabela
    def __str__(self):
        return self.name

class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='item',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        #organizando as categorias por nomes
        ordering=('name',)
        verbose_name_plural='Items'
    #apresentação dos nomes das categorias na tabela
    def __str__(self):
        return self.name
