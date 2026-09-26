from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404,ListCreateAPIView
# from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework import status
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from myapp.serializers import UserSerializer
from myapp.models import User
from myapp.forms import UserForm

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_auth(request):

    return Response({
        'message':'Authentication completed,logged in'
    })

class allAccessView(APIView):

    permission_classes = [AllowAny]

    def get(self,request):

        return Response({
            'message':'Anonymous User'
        })

class AdminView(APIView):

    permission_classes[IsAdminUser]

    def get(self,request):

        return Response({
            'message':'Verified Admin'
        })

class auth_readView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):

        return Response({
            'message':'Auth or readOnly'
        })

class User_gen_permView(ListCreateAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

class User_modelViewset_permView(ModelViewSet):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]