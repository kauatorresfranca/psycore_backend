from django.urls import path
from . import views 

urlpatterns = [
    # Rota para Pacientes
    path('pacientes/', views.paciente_list_create, name='pacientes'),
    
    # Rota para Sessões
    path('sessoes/', views.sessao_list_create, name='sessoes'),
]