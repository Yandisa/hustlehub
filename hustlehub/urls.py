"""
URL configuration for HustleHub project.

Routes URLs to views using function or class-based patterns.
For more details:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ------------------------------------------------------------------------------
# Core URL Patterns
# ------------------------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface

    # App URL configs
    path('', include('home.urls')),              # Public pages
    path('marketplace/', include('marketplace.urls')),  # Listings
    path('users/', include('users.urls')),       # Auth & profiles
]

# ------------------------------------------------------------------------------
# Media Files (Only in Debug Mode)
# ------------------------------------------------------------------------------

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
