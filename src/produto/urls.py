from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('cadastra_pedido/', views.cadastra_produto, name='cadastra_produto'),
    path('exibe_pedido/<int:id>/', views.exibe_produto, name='exibe_produto'),
    path('edita_pedido/<int:id>/', views.edita_produto, name='edita_produto'),
    path('remove_pedido/', views.remove_produto, name='remove_produto'),
    path('pesquisa_pedido/', views.pesquisa_produto, name='pesquisa_produto'),
    path('lista_pedido/', views.lista_produto, name='lista_produto'),
    path('mostra_item/', views.mostra_produto, name='mostra_produto'),
    path('cadastra_carrinho/<int:id>', views.cadastra_carrinho, name='cadastra_carrinho'),
    path('exibe_carrinho/', views.exibe_carrinho, name='exibe_carrinho'),
    path('exibe_lista_carrinho/', views.exibe_lista_carrinho, name='exibe_lista_carrinho'),
    path('atualiza_carrinho/', views.atualiza_carrinho, name='atualiza_carrinho'),
    path('remove_do_carrinho/', views.remove_do_carrinho, name='remove_do_carrinho'),
    # cadastra_produto
    # exibe_produto
    # edita_produto
    # remove_produto
]
