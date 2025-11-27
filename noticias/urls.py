from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from noticias.views import noticias, noticias_detalhes, retornar, todas_noticias
from noticias.views import autores
from noticias.views import buscar
from setup.settings import MEDIA_ROOT

urlpatterns = [
    path('',noticias,name="noticias"),
    path('autor/',autores),
    path("buscar",buscar, name="buscar"),
    path("retornar", retornar, name="retornar"),
    path('<int:noticia_id>/', noticias_detalhes, name='noticias_detalhes'),
    path('noticias/', todas_noticias, name='todas_noticias'),
]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)