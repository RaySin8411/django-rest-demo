from django.urls import path
from .views import FoodDetailAPIView, FoodListCreateAPIView

urlpatterns = [
    path("food/", FoodListCreateAPIView.as_view(), name="food-list"),
    path("food/<int:pk>/", FoodDetailAPIView.as_view(), name="food-detail")
]
