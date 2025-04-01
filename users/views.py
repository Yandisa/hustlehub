from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from marketplace.models import Product
from .forms import CustomUserCreationForm


def register(request):
    """
    Handles user registration using a custom form that collects
    email in addition to username and password.

    On successful registration, logs in the user and redirects
    to their profile.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Registration successful! Welcome to HustleHub."
            )
            return redirect("profile")
        else:
            messages.error(
                request,
                "Registration failed. Please correct the errors below."
            )
    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """
    Displays the user's profile with stats like the number
    of products they've listed.

    Additional metrics (e.g., messages, sales) can be added later.
    """
    products = Product.objects.filter(seller=request.user)
    product_count = products.count()

    return render(request, "users/profile.html", {
        "product_count": product_count,
        "user": request.user,
    })
