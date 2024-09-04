from rest_framework import serializers
from image.models import Image

class ImageSerializer(serializers.ModelSerializer):
    get_image_url = serializers.SerializerMethodField()
    class Meta:
        model=Image
        fields=(
            "id",
            "object_id",
            "title",
            "description",
            "image",
            "is_main",
            "content_type",
            "get_image_url"
            )
    
    def get_get_image_url(self, obj):
        request = self.context.get('request')
        url = request.build_absolute_uri(obj.image.url)
        return url.replace(request.build_absolute_uri('/'), request.build_absolute_uri('/api/references/'))