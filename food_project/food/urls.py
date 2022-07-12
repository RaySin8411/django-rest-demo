from django.urls import path
from .views import FoodDetailAPIview, FoodListCreateAPIView

urlpatterns = [
    path("food/", FoodListCreateAPIView.as_view(), name="food-list"),
    path("food/<int:pk>/", FoodDetailAPIview.as_view(), name="food-detail")
]
