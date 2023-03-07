from django.shortcuts import render
#importando os modelos de categoria e item para apresentalos na site
from item.models import Category,Item

def index(request):
    #fazendo a importação dos produtos q ainda não foram marcados como vendidos
    item=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{'categories':categories,'items':item,})

def contato(request):
    return render(request,'core/contato.html')

