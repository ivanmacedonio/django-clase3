from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.http import JsonResponse
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404


@csrf_exempt
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return JsonResponse(serialized_products.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialized_data = ProductSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=201)
        return JsonResponse(serialized_data.error, status=400)


@csrf_exempt
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        serialized_data = ProductSerializer(product)
        return JsonResponse(serialized_data.data)
    if request.method == "PUT":
        data = JSONParser().parse(request)
        serialized_data = ProductSerializer(product, data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse(serialized_data.data, status=200)
        return JsonResponse(serialized_data.errors, status = 400)
    if request.method == "DELETE":
        product.delete()
        return JsonResponse({"message": "Producto eliminado correctamente..."})
