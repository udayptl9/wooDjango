from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from woocommerce import API
import pprint

wcapi = API(
    url="https://darshanscommunication.com/",
    consumer_key="ck_cebabc4fbb13f3a5ac2cb0c9011952e7a793e6cf",
    consumer_secret="cs_c1dfab0c9edf5c912d2cccd852b93dba9f3ca3ee",
    wp_api=True,
    version="wc/v3"
)

def products(request):
    search = request.GET.get('search', 1)
    per_page = request.GET.get('per_page', 10)
    page = request.GET.get('page', 1)
    r = wcapi.get(f'products?search={search}&page={page}&per_page={per_page}').json()
    context = {
        'products': r
    }
    return render(request, 'app/index.html', context)

def product_update(request, id):
    r = wcapi.get(f'products/{id}').json()
    if request.method == "POST":
        price = request.POST.get('price')
        stock_quantity = request.POST.get('stock_quantity')
        data = {
            "regular_price": price,
            "stock_quantity": stock_quantity
        }
        wcapi.put(f"products/{id}", data)
        return redirect(f'/product/{id}')
    context = {
        'product': r,
    }
    return render(request, 'app/update_product.html', context)