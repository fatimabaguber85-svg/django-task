from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    RegisterView,
    CustomLoginView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    delivery_api,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('api/delivery/', delivery_api, name='delivery_api'),
]