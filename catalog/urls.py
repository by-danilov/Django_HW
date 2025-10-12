from django.urls import path
from django.views.decorators.cache import cache_page # <-- НОВЫЙ ИМПОРТ
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/unpublish/<int:pk>/', views.ProductUnpublishView.as_view(), name='product_unpublish'),
    path('product/<int:pk>/', cache_page(60)(views.ProductDetailView.as_view()), name='product_detail'),
    path('category/<int:pk>/products/', views.CategoryProductListView.as_view(), name='category_products'),
]
