from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Shown in responses, but the client can't set it
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Product
        fields = ["id", "name", "price", "owner", "created_at"]