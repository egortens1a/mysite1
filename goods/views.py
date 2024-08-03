from django.shortcuts import render

import goods
from goods.models import Categories, Products

# Create your views here.
def catalog(request):

    goods = Products.objects.all()

    context = {
        'title':'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods\catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods\product.html', context=context)