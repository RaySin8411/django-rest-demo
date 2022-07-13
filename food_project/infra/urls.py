from django.urls import path
from .view import *

urlpatterns = [
    path('index/', views.index, name='index'),
    path(r'about/', views.about, name='about'),
]
