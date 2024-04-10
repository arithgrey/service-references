from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Enid Service Docs",
        terms_of_service="",
        contact=openapi.Contact(email="jmedrano9006@gmail.com"),        
    ),
    public=True,  # Cambia public a True para permitir acceso público
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/business/', include('business.urls')),
    path('api/image/', include('image.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('uploads/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    
    # Ruta para la raíz del sitio
    path('', RedirectView.as_view(url='/docs/', permanent=False)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
