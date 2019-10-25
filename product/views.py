from django.shortcuts import render, get_object_or_404
from product.models import Item, Tag

def product_detail(request, slug):
   item = get_object_or_404(Item, slug__iexact=slug)
   return render(request, template_name='product/product_detail.html', context={'item': item})



