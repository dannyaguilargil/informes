"""
URL configuration for informes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('login', views.home, name='inicio'),
    path('', views.home, name='casita'),
    ########
    #path('informe/listado_informe', views.listado_informe, name='listado_informe'),
    #path('informe', views.informes, name='informe'), #vista django pasarla a vuejs
    #path('informe/actualizar/<int:id>', views.informeactualizar, name='informeactualizar'),
    #path('informe/listado', views.listado, name='listado'), #solo django
    #path('informe/eliminar', views.informeeliminar, name='informeeliminar'), 
    #path('informe/', views.listado, name='listado'), #solo django
    #path('informe/ente-control', views.entecontrols, name='entecontrol'), #solo django
    #path('informe/listado_ente', views.listadoente, name='listadoente'), #JSON ente de control
    #path('informe/dependencias', views.dependencias, name='dependencias'), #solo django
    #path('informe/listado_dependencia', views.listadodependencia, name='listadodependencia'), #JSON dependencia
    #path('informe/entrega/<int:id>', views.entregar, name='entrega'), 
    #path('informe/nombre_responsable', views.obtener_nombre_responsable, name='nombre_responsable'),
    #path('informe/prueba', views.prueba, name='informeprueba'),
]
