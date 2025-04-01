from django.urls import path
from .views import (
    product_detail,
    my_listings,
    edit_product,
    delete_product,
    post_listing,
    contact_seller,
    category_view,
)

# URL patterns for the marketplace app.
# Handles listing creation, detail views, editing,
# deleting, category filtering, and messaging.

urlpatterns = [
    path(
        "category/<str:category_name>/",
        category_view,
        name="category"
    ),  # Filter listings by category

    path(
        "post-listing/",
        post_listing,
        name="post_listing"
    ),  # Create a new product listing

    path(
        "product/<int:product_id>/",
        product_detail,
        name="product_detail"
    ),  # View product details

    path(
        "product/<int:product_id>/edit/",
        edit_product,
        name="edit_product"
    ),  # Edit a product (owner only)

    path(
        "product/<int:product_id>/delete/",
        delete_product,
        name="delete_product"
    ),  # Delete a product (owner only)

    path(
        "product/<int:product_id>/contact/",
        contact_seller,
        name="contact_seller"
    ),  # Contact product seller

    path(
        "my-listings/",
        my_listings,
        name="my_listings"
    ),  # View listings by logged-in user
]
