from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .permissions import IsOwnerOrAdmin
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ("list", "retrieve"):      # GET → anyone
            return [AllowAny()]
        if self.action == "create":                  # POST → logged-in users
            return [IsAuthenticated()]
        # update, partial_update, destroy → owner or admin
        return [IsAuthenticated(), IsOwnerOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)