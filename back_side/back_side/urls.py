from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('', include('user.urls')),
    path('', include('planning.urls')),
    path('', include('presence.urls')),
    path('', include('note.urls')),
    path('', include('doc.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
