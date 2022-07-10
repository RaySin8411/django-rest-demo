from django.urls import path
from .views import product_api_view

urlpatterns = [
  path("products/<int:pk>/", product_api_view, name="product")
]