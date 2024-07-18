from django.db import models
from .categorias import Categorias
from .diretores import Diretores
from .produtoras import Produtoras

class Filmes(models.Model):
    titulo = models.TextField(null=False)
    diretor = models.ManyToManyField(Diretores)
    categoria = models.ManyToManyField(Categorias)
    produtora = models.ManyToManyField(Produtoras)
    ano = models.IntegerField(null=False)
    pais = models.TextField(null=False)