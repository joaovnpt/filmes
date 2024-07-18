from django.db import models

class Diretores(models.Model):

    nome = models.TextField(null=False)

    def __str__(self):
        return self.nome