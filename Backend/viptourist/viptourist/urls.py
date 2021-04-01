from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('tours/', include('tours.urls')),
    path('main/', include('mainapp.urls')),
    path('sellers/', include('seller.urls')),
    path('yauth/', include('djoser.urls')),
    path('yauth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
