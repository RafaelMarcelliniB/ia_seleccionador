"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gestionador import views

urlpatterns = [
    path('', views.pagina_principal_view, name='pagina_principal'),
    path('estadisticas/', views.estadisticas_mensuales, name='estadisticas_mensuales'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('selector/', views.selector_ia, name='selector_ia'),
    path('selector_log/', views.selector_ia_log, name='selector_ia_log'),
    path('pagina_principal', views.pagina_principal_log, name='pagina_principal_log'),
    path('registro/', views.registrar_usuario, name='registro'),

]