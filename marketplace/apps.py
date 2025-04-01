from django.apps import AppConfig


class MarketplaceConfig(AppConfig):
    """
    Configuration class for the 'marketplace' Django app.

    This app handles all marketplace-related functionality including:
    - Creating, editing, and deleting product listings
    - Viewing listings and product details
    - Category filtering and messaging between users
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace'
