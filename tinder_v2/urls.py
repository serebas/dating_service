"""
URL configuration for tinder_v2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from dating.views import register_user, ClientListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/clients/create/',  register_user),
    #http://127.0.0.1:8000/api/clients/create/

    re_path(r'^auth/', include('djoser.urls.authtoken')),
    #http://127.0.0.1:8000/auth/token/login/
    #http://127.0.0.1:8000/auth/token/logout/

    path('api/list/', ClientListAPIView.as_view(), name='list_client'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
