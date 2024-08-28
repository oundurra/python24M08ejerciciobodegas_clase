"""
URL configuration for bodegas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from main.views import register, index, add_like, remove_like, cotizacion, agrega_bodega

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("",index, name="home"),
    path("cotizacion/",cotizacion, name="cotizacion"),
    path("agrega_bodega/",agrega_bodega, name="agrega_bodega"),
    path("add_like/<int:user_id>/<int:noticia_id>/",add_like, name="add_like"),
    path("remove_like/<int:user_id>/<int:noticia_id>/",remove_like, name="remove_like"),
    path('register/', register, name='register'),
]
