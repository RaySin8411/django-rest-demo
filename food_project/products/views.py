from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view(["GET", "PUT", "DELETE"])
def product_api_view(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
