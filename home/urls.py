from django.urls import path
from . import views

# URL patterns for the 'home' app
# These routes handle general public pages like the homepage,
# search functionality, and the about page.

urlpatterns = [
    path("", views.index, name="home"),  # Homepage: shows all listings
    path("search/", views.search_results, name="search"),  # Search results
    path("about/", views.about, name="about"),  # Static 'About Us' page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
