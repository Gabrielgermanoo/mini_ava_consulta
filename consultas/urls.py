from django.urls import path
from . import views

urlpatterns = [
    path('consultar-usuarios/', views.realizar_consulta, name='consultar_usuarios'),
]