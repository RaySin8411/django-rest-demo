from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class FoodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = FOod.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
