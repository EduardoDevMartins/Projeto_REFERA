from django.db import models
from django.utils import timezone


class categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class modelo(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    Servico = models.CharField(max_length=40)   
    Diagnostico = models.CharField(max_length=255, blank=True)
    Solucao = models.CharField(max_length=800, blank=True)
    Orcamento = models.CharField(max_length=255, blank=True)
    Preco_ideal = models.CharField(max_length=20, default="R$")
    Preco_max = models.CharField(max_length=20, default="R$")
    Categoria = models.ForeignKey(categoria, on_delete=models.DO_NOTHING)
    Padrao = models.ForeignKey(modelo, on_delete=models.DO_NOTHING, default="")
    Ativo = models.BooleanField(default=True)
    Fornecedor = models.CharField(max_length=255, blank=True)
    foto = models.ImageField(blank=True, upload_to='foto/%Y/%m/%d')

    def __str__(self):
        return self.Servico
