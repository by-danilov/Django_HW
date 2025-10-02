# catalog/views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.owner = self.request.user  # Назначаем текущего пользователя
            self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')


    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user



    def handle_no_permission(self):
        return redirect('home')



class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('home')
    template_name = 'catalog/product_confirm_delete.html'

    def test_func(self):
        user = self.request.user
        product = self.get_object()

        is_owner = product.owner == user
        is_moderator = user.has_perm('catalog.delete_product')

        return is_owner or is_moderator

    def handle_no_permission(self):
        return redirect('home')


class ProductUnpublishView(PermissionRequiredMixin, View):
    """
    Контроллер для отмены публикации продукта (для модераторов).
    """
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.is_published:
            product.is_published = False
            product.save()

        return redirect('product_detail', pk=pk)


    def get(self, request, pk):
        return redirect('product_detail', pk=pk)


class ContactsView(ListView):
    pass
