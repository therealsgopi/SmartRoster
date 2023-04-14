from rest_framework import serializers
from .models import class_image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = class_image
        fields = '__all__'