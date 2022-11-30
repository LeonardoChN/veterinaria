"""EVALUACION2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from APLICACION import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('func/',views.listarfuncionario,),
    path('citas/',views.listarcitas),
    path('clientes/',views.listarcliente),
    

    
    path('addmedicos/',views.agregarfun),
    path('addcitas/',views.agregarcitas),
    path('addpacientes/',views.agregarcliente),
    path('addmasc/',views.agregarmascota),

    path('addatencion/',views.agregaratencion),
    
    path('addtipo/',views.agregartipomascota),
    path('addraza/',views.agregarraza),

    path('editarcitas/<int:id>', views.actualizarcitas),
    path('editarmedicos/<int:id>', views.actualizarfuncionario),
    path('editarpacientes/<int:id>', views.actualzarcliente),

    
    path('eliminarcitas/<int:id>', views.eliminarcitas),
    path('eliminarfuncionario/<int:id>', views.eliminarfuncionario),
    path('eliminarcliente/<int:id>', views.eliminarcliente),

    


    


    


    


]
