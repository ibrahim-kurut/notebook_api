
from rest_framework import serializers
from .models import Notebook

class NotebookSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Notebook
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at']