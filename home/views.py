from django.shortcuts import render
from products.models import Product, Comment


def index(request):
    """
    A view to return the index page
    """

    products = Product.objects.all()
    featured_products = list(Product.objects.filter(featured=True).order_by(
        'featured'))[-9:-1][::-1]  # show recent 8 featured products
    # show recently added 8 products
    recently_added = products.order_by('-id')[:8]

    comments = Comment.objects.all().order_by('-id')[:10]
    context = {
        'products': products,
        'featured_products': featured_products,
        'recently_added': recently_added,
        'comments': comments
    }

    return render(request, 'home/index.html', context)
