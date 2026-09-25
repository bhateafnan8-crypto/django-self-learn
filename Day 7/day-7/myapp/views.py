from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Product
# Create your views here.

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'


@api_view(['GET'])
def product_list(request):

    return Response({
        'message':'RestApiView:- Product Api'
    })

@api_view(['POST'])
def create_products(request):

    serializer = ProductSerializer(data = request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)
    
@api_view(['GET'])
def products_lst(request):

    products_lst = Product.objects.all()

    serializer = ProductSerializer(products_lst,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_product_byID(request,id):
    product_byId = Product.objects.get(id=id) #use always get here because this is for single_object_api ..which will be use get method for getting data from db

    serializer = ProductSerializer(product_byId)

    return Response(serializer.data)

@api_view(['PUT'])
def edit_product(request,id):
    product_byId = Product.objects.get(id=id)
    serializer = ProductSerializer(product_byId,data = request.data)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)
@api_view(['PATCH'])
def partial_edit_product(request,id):
    product_byId = Product.objects.get(id=id)
    serializer = ProductSerializer(product_byId,data = request.data,partial=True)

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['DELETE'])
def dlt_prod(request,id):

    prod = Product.objects.get(id = id)

    prod.delete() 

    return Response({'messgae':'Product deleted successfully'})