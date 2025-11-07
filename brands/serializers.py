from rest_framework import serializers

from .models import Brand


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
