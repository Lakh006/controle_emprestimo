from django.urls import path
from app_emprestimo import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cadastrar/', views.cadastrar_colaborador, name='cadastrar'),
    path('listar/', views.listar_colaboradores, name='listar_colaboradores'),
    path('atualizar/<int:idCOLABORADOR>',views.atualizar_colaborador, name='atualizar_colaborador'),
    path('deletar/<int:idCOLABORADOR>', views.deletar_colaborador, name='deletar_colaborador'),
]
