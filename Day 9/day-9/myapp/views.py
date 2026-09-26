from django.shortcuts import render
from rest_framework import status
from myapp.serializers import UserSerializer
from myapp.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny,BasePermission 


# Create your views here.

class ProfileView(APIView):

    def get(self,request):
        if request.user.is_authenticated:
            return Response({
                "username":request.user.username
            })

        return Response({
            'message':'Please login first'
        })

class ProfilesView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        return Response({
            'message':'Welcome',
            'user':request.user.username
        })

class HomeView(APIView):

    permission_classes = [AllowAny]

    def get(self,request):

        return Response({
            'message':'Your Home Page allow any/all'
        })

class AdminView(APIView):

    permission_classes = [IsAdminUser]

    def get(self,request):

        return Response({
            'message':'Your Admin Page'
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users(request):

    return Response({
        'message':'Welcome,you are loggedIn',
        'user':request.user.username
    })

class DashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):

        return Response({
            'message':'Welcome to your dashboard'
        })

class isOwner(APIView):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.owner