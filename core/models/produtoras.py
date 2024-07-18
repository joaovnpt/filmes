from django.db import models

class Produtoras(models.Model):

    nome = models.TextField(null=False)

    def __str__(self):
        return self.nome