from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from catalog.models import Product
from catalog.forms import ProductForm
from django.urls import reverse_lazy

class ProductListView(ListView):
    # Эта страница должна быть доступна всем, поэтому здесь нет LoginRequiredMixin
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('users:login') # Перенаправляем на страницу входа

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('users:login')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('users:login')

# Контакты остаются без изменений, так как не требуют авторизации
class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'
