from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="todo-home"),
    path('<int:id>/edit/', views.update, name="todo-update"),
    path('<int:id>/delete/', views.delete, name="todo-delete")
    
]
