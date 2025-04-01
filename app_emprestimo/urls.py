from django.urls import path
from app_emprestimo import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastrar/', views.cadastrar_colaborador, name='cadastrar'),
]
