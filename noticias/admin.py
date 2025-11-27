from django.contrib import admin

import noticias.models as nt

# Register your models here.
admin.site.register(nt.Categoria)
admin.site.register(nt.Autor)
admin.site.register(nt.Noticia)
