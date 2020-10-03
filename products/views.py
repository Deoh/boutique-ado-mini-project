from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()  # gets all products from the database

    """ 'products' is added to context so that the products will be avaliable to the template """
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)  # context is used here to send 'products' to the temmplate


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)  # gets an individual product with id from the database

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
