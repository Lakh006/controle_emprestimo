from django.urls import path
from app_emprestimo import views

#urls necessárias
urlpatterns = [
    path('', views.home, name="home"),
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'), 
    path('cadastrar_gerente/', views.cadastro_gerente, name='cadastrar_gerente'),
    path('cadastrar_colaborador/', views.cadastrar_colaborador, name='cadastrar_colaborador'),
    path('cadastrar_emprestimo/', views.cadastrar_emprestimo, name='cadastrar_emprestimo'),
    path('atualizar_emprestimo/<int:idEMPRESTIMO>', views.atualizar_emprestimo, name='atualizar_emprestimo'),
    path('listar_equipamento/', views.listar_equipamento, name='listar_equipamento'),
    path('atualizar_equipamento/<int:idEPI>', views.atualizar_equipamento, name='atualizar_equipamento'),
    path('deletar_equipamento/<int:idEPI>', views.deletar_equipamento, name='deletar_equipamento'),
    path('login/', views.login_request, name='login'), #terminar
    path('listar_relatorio/', views.listar_relatorio, name='listar_relatorio'),
    path('listar_colaborador/', views.listar_colaborador, name='listar_colaborador'),
    path('atualizar/<int:idCOLABORADOR>',views.atualizar_colaborador, name='atualizar_colaborador'),
    path('deletar/<int:idCOLABORADOR>', views.deletar_colaborador, name='deletar_colaborador'),
]
