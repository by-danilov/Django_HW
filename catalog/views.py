from django.shortcuts import render, get_object_or_404
from .models import Product


def home_page(request):
    products = Product.objects.all()  # Получаем все продукты из БД
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html', context)


def contacts_page(request):
    # Эта функция будет рендерить страницу контактов
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    # Используем get_object_or_404, чтобы получить товар или вернуть ошибку 404, если он не найден
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)
