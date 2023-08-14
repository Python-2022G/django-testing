from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated



class ProductList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    