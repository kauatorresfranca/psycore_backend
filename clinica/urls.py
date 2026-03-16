from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views 

urlpatterns = [
    # Rota para Login (Gera o Token)
    # O Front-end fará um POST para /api/login/ enviando username e password
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Rota para Atualizar o Token (Refresh)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Suas rotas existentes
    path('pacientes/', views.paciente_list_create, name='pacientes'),
    path('sessoes/', views.sessao_list_create, name='sessoes'),
    path('sessoes/<int:pk>/', views.sessao_detail, name='sessao_detail'),
    path('dashboard/stats/', views.dashboard_view, name='dashboard'),
]