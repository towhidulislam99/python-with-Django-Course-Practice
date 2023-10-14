"""
URL configuration for demo project.

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
from django.urls import path
from . import views as v

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("demo/", v.index, name='demo_index'),
    path("user/", v.user, name='user_index'),
    path("user/<int:id>", v.edit_index, name='edit_index'),
    path("update/", v.update, name='update_index'),
    path("demo/<int:id>", v.delete_index, name='delete_index'),
     
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
