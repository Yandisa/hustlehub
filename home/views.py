from django.shortcuts import render
from marketplace.models import Product


def index(request):
    """
    Renders the homepage displaying all product listings.

    Retrieves all products from the database and passes them
    to the 'home/index.html' template.
    """
    products = Product.objects.all()
    return render(request, 'home/index.html', {
        'products': products
    })


def search_results(request):
    """
    Renders search results based on user query.

    If a query is provided in the URL's GET parameters,
    it filters products by name (case-insensitive).
    If no query is provided, returns an empty list.
    """
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) \
        if query else []

    return render(request, 'home/search_results.html', {
        'products': products,
        'query': query
    })


def about(request):
    """
    Renders the static 'About Us' page.
    """
    return render(request, "home/about.html")
