from django.contrib import admin
from django.urls import include, path
from .import views
urlpatterns = [
    path("login",views.login,name="login"),
    path("register", views.register, name="register"),
    path("logout",views.logout,name="logout"),
    path("confirm", views.confirm,name="confirm"),
    # path("SecondPage",views.SecondPage, name="SecondPage")
]      