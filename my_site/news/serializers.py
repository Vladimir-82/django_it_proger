from rest_framework import serializers
from .models import Articles


class Articles_serializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'anons', 'full_text', 'date')