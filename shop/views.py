from django.shortcuts import render
from product.models import Item, Tag

def index(request):
   items = Item.objects.all()
   return render(request, template_name='shop/index.html', context={'items': items})