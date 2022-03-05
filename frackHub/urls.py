from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='frackHub_home'),
    path('about/', views.about, name='frackHub_about'),
]
