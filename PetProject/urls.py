from django.contrib import admin
from django.urls import path, include

from utils.swagger import schema_view

from PetProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
    ]
