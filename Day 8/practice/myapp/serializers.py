from rest_framework import serializers
from myapp.models import Product

class ProdcutSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'