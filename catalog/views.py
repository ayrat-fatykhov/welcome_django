from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def show_product(request, pk):
    context = {'object': Product.objects.get(pk=pk)}
    return render(request, 'catalog/show_product.html', context)
