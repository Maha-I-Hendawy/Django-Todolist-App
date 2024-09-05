from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="users-index"),
    path('adduser/', views.adduser, name="users-add-user"),
    path('login/', views.login, name="users-login"),
    path('profile/', views.profile, name="users-profile")
]
