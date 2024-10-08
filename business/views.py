from django.shortcuts import get_object_or_404
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from business.models import Business
from image.serializers import ImageSerializer
from django.core.cache import cache

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000

class BusinessSlugImagesViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=['GET'])    
    def images_by_slug(self, request, business_slug): 
        cache_key = f'bussines_image_{business_slug}_page_{request.query_params.get("page")}'
        cache_data = cache.get(cache_key)
        if cache_data is not None:
            return Response(cache_data)
            
        business = get_object_or_404(Business, slug=business_slug)
        images_qs = business.images.all().order_by('id')
        
        # Use custom pagination class
        paginator = CustomPageNumberPagination()
        page = paginator.paginate_queryset(images_qs, request)
        
        if page is not None:
            # Pasar el contexto del request al serializador
            serializer = ImageSerializer(page, many=True, context={'request': request})
            response = paginator.get_paginated_response(serializer.data)
            cache.set(cache_key, response.data, timeout=60 * 60 * 240) 
            return response

        # También pasar el contexto aquí en caso de no paginación
        serializer = ImageSerializer(images_qs, many=True, context={'request': request})
        response = Response(serializer.data)
        cache.set(cache_key, response.data, timeout=60 * 60 * 240)
        return response
