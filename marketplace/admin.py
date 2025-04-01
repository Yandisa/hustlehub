from django.contrib import admin
from .models import Product

# Register the Product model with the Django admin site.
# This allows admins to create, update, and delete products
# via the built-in admin interface.

admin.site.register(Product)
