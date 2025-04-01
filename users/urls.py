from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# URL patterns for user-related functionality:
# - Registration, login, logout
# - Profile view
# - Password reset flow (optional)

urlpatterns = [
    # Registration and profile
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Authentication (login/logout)
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html",
            next_page="profile"
        ),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout"
    ),

    # Optional: Password reset functionality
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset"
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
]
