from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Cliente
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib import messages

def index(request):
    Clientes = Cliente.objects.order_by('Categoria')
    paginator = Paginator(Clientes, 15)

    page = request.GET.get('page')
    Clientes = paginator.get_page(page)

    return render(request, 'clientes/index.html', {
        'Clientes': Clientes
    })


def ver_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente,id=cliente_id)

    if not cliente.Ativo:
        raise Http404()

    return render(request, 'clientes/ver_cliente.html', {
        'cliente': cliente
    })
    

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        # messages.add_message(request, messages.ERROR, 'O campo pesquisa não pode ficar vazio')
        return redirect('index')

    Clientes = Cliente.objects.order_by('Categoria').filter(
        Q(Servico__icontains=termo) | Q(Diagnostico__icontains=termo),
        Ativo=True
        
    )
        

    paginator = Paginator(Clientes, 15)
   
    page = request.GET.get('page')
    Clientes = paginator.get_page(page)

    return render(request, 'clientes/busca.html', {
        'Clientes': Clientes
    })

    

