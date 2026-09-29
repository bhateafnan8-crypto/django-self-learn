# accounts/views.py
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


# Create your views here.

class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self,request):

        serializer = RegisterSerializer(data = request.data)

        serializer.is_valid(raise_exception= True)

        user = serializer.save()
        token,_ = Token.objects.get_or_create(user=user)

        return Response(
            {
            'username':user.username,'token':token.key
            },
            status= status.HTTP_201_CREATED,
        )

class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self,request):

        user = authenticate(
            username = request.data.get("username"),
            password = request.data.get("password"),
        )

        if user is None:

            return Response(
                {
                'error':'Invalid credentials'
                
                },
                status = status.HTTP_400_BAD_REQUEST
            )

        token,_ = Token.objects.get_or_create(user=user)

        return Response({
            'token':token.key
        })
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        request.user.auth_token.delete()

        return Response(status= status.HTTP_204_NO_CONTENT)

