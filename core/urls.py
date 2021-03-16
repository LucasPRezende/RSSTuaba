from django.urls import path

from .views import index, registrar, leitor
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('contas/', include('django.contrib.auth.urls')),

    path('leitor', leitor, name='leitor'),
    path('registrar/', registrar, name='registrar'),
]