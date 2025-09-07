from django.shortcuts import render


def home_page(request):
    # Эта функция будет рендерить (отображать) главную страницу
    return render(request, 'catalog/home.html')


def contacts_page(request):
    # Эта функция будет рендерить страницу контактов
    return render(request, 'catalog/contacts.html')
