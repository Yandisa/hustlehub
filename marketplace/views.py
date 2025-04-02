from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Product
from .forms import ProductForm, ContactSellerForm


@login_required(login_url="login")
def post_listing(request):
    """
    Allows a logged-in user to create a new product listing.

    GET – Show the form to create a listing.
    POST – Save listing and redirect to 'My Listings'.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(
                request, "Your product has been listed successfully!"
            )
            return redirect("my_listings")
    else:
        form = ProductForm()

    return render(request, "marketplace/post_listing.html", {
        "form": form
    })


def category_view(request, category_name):
    """
    Displays all products within a specific category.
    """
    products = Product.objects.filter(category=category_name)

    return render(request, "marketplace/category.html", {
        "category": category_name.capitalize(),
        "products": products,
    })


def product_detail(request, product_id):
    """
    Displays detailed information about a specific product.
    """
    product = get_object_or_404(Product, id=product_id)

    return render(request, "marketplace/product_detail.html", {
        "product": product
    })


@login_required
def my_listings(request):
    """
    Displays all products listed by the logged-in user.
    """
    products = Product.objects.filter(
        seller=request.user
    ).order_by("-created_at")

    return render(request, "marketplace/my_listings.html", {
        "products": products
    })


@login_required
def edit_product(request, product_id):
    """
    Allows a user to update one of their product listings.
    
    Arguments:
        request – The HTTP request object.
        product_id – ID of the product to edit.

    Returns:
        Renders the edit form or redirects after update.
    """
    product = get_object_or_404(
        Product, id=product_id, seller=request.user
    )

    if request.method == "POST":
        form = ProductForm(
            request.POST, request.FILES, instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(
                request, "Product updated successfully!"
            )
            return redirect("my_listings")
    else:
        form = ProductForm(instance=product)

    return render(request, "marketplace/edit_product.html", {
        "form": form,
        "product": product
    })


@login_required
def delete_product(request, product_id):
    """
    Deletes a product listing.

    Requires:
        - The user to be the owner of the product.
        - A valid product ID.

    Returns:
        Redirect to 'My Listings' page after deletion.
    """
    product = get_object_or_404(
        Product, id=product_id, seller=request.user
    )

    if request.method == "POST":
        product.delete()
        messages.success(
            request, "Product deleted successfully!"
        )
        return redirect("my_listings")

    return render(request, "marketplace/delete_product.html", {
        "product": product
    })


@login_required
def contact_seller(request, product_id):
    """
    Lets a user contact the seller of a specific product via email.
    """
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ContactSellerForm(request.POST)
        if form.is_valid():
            # Avoid sending blank or invalid email if user's email is missing
            sender_email = request.user.email or "noreply@hustlehub.com"

            send_mail(
                subject=f"Interest in {product.name}",
                message=form.cleaned_data["message"],
                from_email=sender_email,
                recipient_list=[product.seller.email],
            )
            messages.success(
                request, "Your message has been sent to the seller!"
            )
            return redirect("product_detail", product_id=product.id)
    else:
        form = ContactSellerForm()

    return render(request, "marketplace/contact_seller.html", {
        "form": form,
        "product": product
    })
