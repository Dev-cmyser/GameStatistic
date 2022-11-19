from django.contrib.auth import views as auth_views
from .views import *
from django.urls import path


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('get_data/', get_data, name="get_data"),
    path('logarifm/', logarifm, name="logarifm"),
    path('', main_graf, name="graf"),
]
