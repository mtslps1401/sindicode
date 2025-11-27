from django.shortcuts import render, get_object_or_404
from noticias.models import Categoria, Noticia
from noticias.models import Autor
from django.db.models import Q


# funcao
# se def dentro classe = metodo
# se def fora classe = função

# Create your views here.

def categorias(request):
    # definindo um mock com dict

    categorias = Categoria.objects.all()
    return render(request,
    'noticias/index.html',
          {'cards':categorias})

def noticias(request):
        noticias = Noticia.objects.all()
        return render(request,'noticias/index.html',{'noticias':noticias})


def autores(request):
    autores = Autor.objects.all()
    return  render(request,'noticias/nossos_autores.html',{'autores':autores})


def buscar(request):
    noticias = Noticia.objects.all()

    if 'buscar' in request.GET:

        nome_buscar = request.GET["buscar"]

        if nome_buscar:
            condicao_titulo = Q(titulo__icontains=nome_buscar)
            condicao_conteudo = Q(conteudo__icontains=nome_buscar)

            filtro_ou =  condicao_titulo | condicao_conteudo
            
            noticias = Noticia.objects.filter(filtro_ou)
        
        else:
            noticias = Noticia.objects.all()
        
    return render(request, 'noticias/buscar.html', {'noticias':noticias})

def retornar(request):

    noticias = Noticia.objects.all()

    return render(request, 'noticias/index.html', {'noticias':noticias})

def noticias_detalhes(request, noticia_id):

    noticias = get_object_or_404(Noticia, pk=noticia_id)

    return render(request, 'noticias/detalhes.html', {'noticia': noticias})



def todas_noticias(request):
    todas_noticias = Noticia.objects.all().order_by('-data_publicacao')

    context = {
        'noticias': todas_noticias,
        'titulo_pagina': 'Todas as Notícias Publicadas'
    }
    return render(request, 'noticias/buscar.html', context)
