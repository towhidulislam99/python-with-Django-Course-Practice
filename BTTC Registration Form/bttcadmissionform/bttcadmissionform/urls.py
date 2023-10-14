"""
URL configuration for bttcadmissionform project.

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
    # path('admin/', admin.site.urls),
    path("index/", v.indexpage, name='index'),
    path("home/", v.homepage, name='form_data'),
    path("output/", v.outputpage, name='output'),
    path("back/", v.backpage, name='logout'),
    path("edit/<int:id>", v.edit_index, name='edit_index'),
    path("update/", v.update, name='update_data'),
    path("output/<int:id>", v.delete_index, name='delete_index'),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Your URL patterns go here

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
