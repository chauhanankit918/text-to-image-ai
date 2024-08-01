from rest_framework import serializers

from myapp.models import TextImage


class TextImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextImage
        fields = ('pk', 'image', 'title')
