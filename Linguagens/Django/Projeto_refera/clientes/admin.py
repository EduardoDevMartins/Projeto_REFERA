from django.contrib import admin
from .models import categoria, Cliente, modelo


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Servico', 'Solucao', 'Padrao', 'Ativo', 'Categoria', 'Preco_ideal', 'Preco_max', 'Fornecedor')
    list_display_links = 'id', 'Servico'
    list_per_page = 10
    search_fields = ('Servico','Categoria')
    list_editable = ('Ativo', 'Solucao', 'Preco_ideal', 'Preco_max')
    


admin.site.register(categoria)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(modelo)
