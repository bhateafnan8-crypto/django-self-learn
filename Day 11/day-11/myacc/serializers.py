# myacc/serializers.py
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only = True, validators = [validate_password] )


    class Meta:

        model = User

        fields =  ["username", "email", "password"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)