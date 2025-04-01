from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configuration class for the 'users' Django app.

    This app manages user-related functionality including:
    - Registration and authentication
    - User login/logout
    - Profile viewing and future profile editing
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
