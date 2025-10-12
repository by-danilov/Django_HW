from .models import Product
from django.core.cache import cache


def get_products_by_category(category_pk):
    """
    Возвращает список всех опубликованных продуктов в указанной категории,
    используя низкоуровневое кеширование.
    """
    cache_key = f'products_cat_{category_pk}'
    product_list = cache.get(cache_key)
    if product_list is None:
        product_list = Product.objects.filter(
            category_id=category_pk,
            is_published=True
        ).select_related('category').order_by('name')
        cache.set(cache_key, product_list, 300)
        print(f"DEBUG: Получено из БД и сохранено в кеш: {cache_key}")
    else:
        print(f"DEBUG: Получено из кеша: {cache_key}")
    return product_list
