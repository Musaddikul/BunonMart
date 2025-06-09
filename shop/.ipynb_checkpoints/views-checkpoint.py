from django.shortcuts import render
from .models import Product

def home(request):
    featured = Product.objects.filter(is_featured=True)[:10]
    men = Product.objects.filter(category="men")
    women = Product.objects.filter(category="women")
    kids = Product.objects.filter(category="kids")
    trending = Product.objects.filter(category="trending")
    new_collection = Product.objects.filter(category="new")

    context = {
        "featured": featured,
        "men": men,
        "women": women,
        "kids": kids,
        "trending": trending,
        "new_collection": new_collection,
    }
    return render(request, "home.html", context)


def products(request):
    products = Product.objects.all()
    search_query = request.GET.get("q")
    if search_query:
        products = products.filter(name__icontains=search_query)

    category_filter = request.GET.getlist("category")
    if category_filter:
        products = products.filter(category__in=category_filter)

    context = {"products": products}
    return render(request, "products.html", context)