# shop/views.py
from django.shortcuts import render
from .models import Product, Category, SubCategory
from django.db.models import Q

def home(request):
    featured = Product.objects.filter(is_featured=True)[:10]
    men = Product.objects.filter(section="men")
    women = Product.objects.filter(section="women")
    kids = Product.objects.filter(section="kids")
    trending = Product.objects.filter(section="trending")
    new_collection = Product.objects.filter(section="new")

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
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    # Search
    search_query = request.GET.get("q")
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Category filter
    selected_category = request.GET.get("category")
    if selected_category:
        products = products.filter(category__slug=selected_category)

    # Subcategory filter
    selected_subcategory = request.GET.get("subcategory")
    if selected_subcategory:
        products = products.filter(subcategory__name__iexact=selected_subcategory)

    # Sorting
    sort_by = request.GET.get("sort")
    if sort_by == "price_low":
        products = products.order_by("price")
    elif sort_by == "price_high":
        products = products.order_by("-price")
    elif sort_by == "newest":
        products = products.order_by("-created_at")

    context = {
        "products": products,
        "categories": categories,
        "subcategories": subcategories,
        "selected_category": selected_category,
        "selected_subcategory": selected_subcategory,
        "search_query": search_query,
        "sort_by": sort_by,
    }
    return render(request, "products.html", context)
