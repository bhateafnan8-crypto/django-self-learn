from django.shortcuts import render
from rest_framework import status
from myapp.serializers import ProdcutSerializer
from myapp.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def products(request):

    if request.method == "GET":
        prods = Product.objects.all()

        serializer = ProdcutSerializer(prods,many=True)

        return Response(serializer.data)

    elif request.method == "POST":

        serializer = ProdcutSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

@api_view(['GET','PUT','PATCH','DELETE'])
def prod_lst(request,id):

    try:

        prods = get_object_or_404(Product,id=id)

    except Product.DoesNotExist:

        return Response({'message':'Product does not exists'})

    if request.method == "GET":

        serializer = ProdcutSerializer(prods)

        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = ProdcutSerializer(prods,data = request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "PATCH":

        serializer = ProdcutSerializer(prods,data = request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "DELETE":

        prods.delete()

        return Response({'message':'Product deleted successfully'})