from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Configuration class for the 'home' Django app.

    This app handles public-facing pages such as:
    - Home (index) page
    - Search functionality
    - Static content pages like 'About'
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
