from django.shortcuts import render

# Create your views here.
def associados(request ):
    return render(request,'associados/index.html')