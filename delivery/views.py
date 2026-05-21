from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Product, Delivery


# Function Based View
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'delivery/product_list.html', {'products': products})


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'delivery/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'delivery/login.html'


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'delivery/product_list.html'
    context_object_name = 'products'
    permission_required = 'delivery.view_product'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'price', 'description']
    template_name = 'delivery/product_form.html'
    success_url = reverse_lazy('products')
    permission_required = 'delivery.add_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'price', 'description']
    template_name = 'delivery/product_form.html'
    success_url = reverse_lazy('products')
    permission_required = 'delivery.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'delivery/product_confirm_delete.html'
    success_url = reverse_lazy('products')
    permission_required = 'delivery.delete_product'


def delivery_api(request):
    deliveries = Delivery.objects.all().values()
    return JsonResponse(list(deliveries), safe=False)