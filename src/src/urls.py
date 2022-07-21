from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user_register.views import *
from rest_framework import routers
from question.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_register.urls')),
    path('answer/', include('answer.urls'), name='answer'),
]

if settings.DEBUG:
    urlpatterns = [
                    path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

