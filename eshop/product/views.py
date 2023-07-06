from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer

from .models import Product

# Create your views here.

@api_view(['GET'])
def get_products(request):

    products =Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response({ 'product': serializer.data })

