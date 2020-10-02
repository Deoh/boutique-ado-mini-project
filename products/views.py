from django.shortcuts import render
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
