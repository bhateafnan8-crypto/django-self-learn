from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # Shown in responses, but the client can't set it
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "created_at"]