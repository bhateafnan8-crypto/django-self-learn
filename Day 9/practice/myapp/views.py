from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,BasePermission 


# Create your views here.


class ProductsView(APIView):

    permission_classes = [AllowAny]

    def get(self,request):

        return Response({
            'message':'Welcome to Product Page'
        })

class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        return Response({
            'message':'Welcome to Profile Page'
        })

class AdminView(APIView):

    permission_classes = [IsAdminUser]

    def get(self,request):

        return Response({
            'message':'Welcome to Admin Page'
        })