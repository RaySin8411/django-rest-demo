from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer


# Create your views here.

class FoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = FOod.objects.all()
    serializer_class = FoodSerializer
