from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "users"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("secret-area/", views.secret_area_view, name="secret_area"),
]
