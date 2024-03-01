from rest_framework import serializers

from .models import VideoRequest


class VideoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRequest
        fields = '__all__'
