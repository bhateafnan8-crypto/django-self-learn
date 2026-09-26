from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Product
from myapp.serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def prod_list(request):

    prods = Product.objects.all()

    serializer = ProductSerializer(prods,many=True)

    return Response(serializer.data)

@api_view(['GET','POST'])
def prod_getpost(request):

    if request.method == "GET":

        prods = Product.objects.all()

        serializer = ProductSerializer(prods,many=True)

        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors)

@api_view(['GET','PUT','PATCH','DELETE'])
def pro_getputpatchdlt(request,id):
    try:
        prod_lst = get_object_or_404(Product,id =id)

    except Product.DoesNotExist:

        return Response({'message': 'Product not found'}, status=404)


    if request.method == "GET":

        serializer = ProductSerializer(prod_lst)
        
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = ProductSerializer(prod_lst,data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)  

        return Response(serializer.errors)  
    
    elif request.method == "PATCH":

        serializer = ProductSerializer(prod_lst,data= request.data,partial=True)    

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "DELETE":

        prod_lst.delete()

        return Response({'message':'Product Deleted Successfully'})
