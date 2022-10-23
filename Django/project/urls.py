from django.contrib import admin
from django.urls import path, include
import core.urls
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('teg', include(core.urls, namespace='core')),
    path('', schema_view),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)
