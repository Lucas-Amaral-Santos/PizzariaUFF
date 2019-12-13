from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from produto.forms import ProdutoForm, RemoveProdutoForm, PesquisaProdutoForm, AtualizaProdutoForm
from produto.models import Produto, Foto, Order, OrderItem
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, FloatField
from django.utils import timezone


def mostra_produto(request):
    fotos = Foto.objects.all()
    produtos = Produto.objects.all()
    return render(request, 'produto/mostrar_produto.html', {'fotos':fotos, 'itens':produtos})

def pesquisa_produto(request):
   form = PesquisaProdutoForm()
   return render(request, 'produto/pesquisa_produto.html', {
      'form': form
   })

def lista_produto(request):
   form = PesquisaProdutoForm(request.GET)
   if (form.is_valid()):
      busca_por = form.cleaned_data['busca_por']
      lista_de_produtos = Produto.objects.filter(nome__icontains=busca_por).order_by('nome')

      resultado = lista_de_produtos.aggregate(
          total=Sum(F('preco'), output_field=FloatField()))
      
      if resultado['total']:
         total = '{0:.2f}'.format(resultado['total'])
      else:
         total = '0,00'

      paginator = Paginator(lista_de_produtos, 5)
      pagina = request.GET.get('pagina')
      produtos = paginator.get_page(pagina)

#      lista_de_forms = []
#      for produto in produtos:
#         lista_de_forms.append(RemoveProdutoForm(initial={'produto_id': produto.id}))

      lista_de_ids = []
      for produto in produtos:
         lista_de_ids.append(produto.id)

      return render(request, 'produto/pesquisa_produto.html', {
         'form': form,
#        'listas': zip(produtos, lista_de_forms),
         'produtos': produtos,
         'lista_de_ids': lista_de_ids,
         'total': total,
         'busca_por': busca_por
      })

   else:
      raise ValueError('Ocorreu um erro inesperado ao tentar pesquisar um produto.')   

# @login_required
def cadastra_produto(request):
    if request.POST:
        produto_id = request.POST.get('produto_id')
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, instance=produto)
        else:
            produto_form = ProdutoForm(request.POST)

        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            if produto_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
            else:
                produto.user = request.user
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            produto.save()
            return redirect('produto:exibe_produto', id=produto.id)
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        produto_form = ProdutoForm()

    fim = datetime.now()   # now() retorna um datetime
                                # now().date() retorna um date
    ano_fim = fim.year
    mes_fim = fim.month
    dia_fim = fim.day

    inicio = fim - timedelta(days=10)
    ano_inicio = inicio.year
    mes_inicio = inicio.month
    dia_inicio = inicio.day

    return render(request, 'produto/cadastra_produto.html', {
       'form': produto_form,
       'ano_fim': ano_fim, 
       'mes_fim': mes_fim, 
       'dia_fim': dia_fim, 
       'ano_inicio': ano_inicio, 
       'mes_inicio': mes_inicio, 
       'dia_inicio': dia_inicio
    })


def exibe_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form_remove_produto = RemoveProdutoForm(initial={'produto_id': id})
    return render(request, 'produto/exibe_produto.html', {
       'produto': produto,
       'form_remove_produto': form_remove_produto
    })


def edita_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto_form = ProdutoForm(instance=produto)
    produto_form.fields['produto_id'].initial = id

    fim = datetime.now()   # now() retorna um datetime
                           # now().date() retorna um date
    ano_fim = fim.year
    mes_fim = fim.month
    dia_fim = fim.day

    inicio = fim - timedelta(days=10)
    ano_inicio = inicio.year
    mes_inicio = inicio.month
    dia_inicio = inicio.day

    return render(request, 'produto/cadastra_produto.html', {
       'form': produto_form,
       'ano_fim': ano_fim, 
       'mes_fim': mes_fim, 
       'dia_fim': dia_fim, 
       'ano_inicio': ano_inicio, 
       'mes_inicio': mes_inicio, 
       'dia_inicio': dia_inicio
    })


def remove_produto(request):
#   form_remove_produto = RemoveProdutoForm(request.POST)
#   if form_remove_produto.is_valid:
      # produto_id = form_remove_produto.cleaned_data['produto_id']
      produto_id = request.POST.get('produto_id')
      produto = get_object_or_404(Produto, id=produto_id)
      if produto.user == request.user:
         produto.delete()
         messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')
      else:
         messages.add_message(request, messages.ERROR, 'Você não tem permissão para remover esse produto.')
      return render(request, 'produto/exibe_produto.html', {'produto': produto})
#   else:
#      raise ValueError('Ocorreu um erro inesperado ao tentar remover um produto.')


#----------------------ADICIONA CARRINHO--------------------------------

def atualiza_produto(request):
   pass

def exibe_carrinho(request):
   order_items = OrderItem.objects.filter(user=request.user, ordered=False)

   resultado = order_items.aggregate(
       total=Sum(F('quantity') * F('price'), output_field=FloatField()))
   
   if resultado['total']:
      total = '{0:.2f}'.format(resultado['total'])
   else:
      total = '0,00'

   lista_de_ids = []
   lista_de_forms = []
   for item in order_items:
      lista_de_ids.append(item.id)
      lista_de_forms.append(AtualizaProdutoForm(initial={'quantity': item.quantity}))

   return render(request, 'produto/carrinho.html', {
      'listas': zip(order_items, lista_de_forms),
      'lista_de_ids': lista_de_ids,
      'total': total
   })

def cadastra_carrinho(request, id):
   item = get_object_or_404(Produto, id=id)
   order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
   order_item.price = item.preco
   order_qs = Order.objects.filter(user=request.user, ordered=False)
   
   if order_qs.exists():
      order = order_qs[0]

      if order.items.filter(item__id=item.id).exists():
         order_item.quantity += 1
         order_item.save()
         messages.info(request, "Adicionado!")
      else:
         order_item.save()
         order.items.add(order_item)

   else:
      ordered_date = timezone.now()
      order = Order.objects.create(user=request.user, ordered_date=ordered_date)
      order_item.save()
      order.items.add(order_item)

   return redirect("produto:exibe_produto", id=id)

def remove_carrinho(request):
   produto_id = request.POST.get('produto_id')
   print(produto_id)
   produto = get_object_or_404(Produto, id=produto_id)
   produto.delete()

   resultado = Produto.objects.all().aggregate(
      total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))
   
   if resultado['total']:
      total = '{0:.2f}'.format(resultado['total'])
   else:
      total = '0,00'

   return render(request, 'produto/valor_do_estoque.html', {
      'total': total
   })
