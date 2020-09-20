from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:id>', views.product_update, name='product_update'),
]