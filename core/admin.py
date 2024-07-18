from django.contrib import admin

from core.models import Categorias

admin.site.register(Categorias)

from core.models import Diretores

admin.site.register(Diretores)

from core.models import Produtoras

admin.site.register(Produtoras)

from core.models import Filmes

admin.site.register(Filmes)