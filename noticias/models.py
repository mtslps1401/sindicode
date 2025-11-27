from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# Estudar o que é orm (object relation mapper)

#Herença é uma classe herda de outra classe e implementa suas próprias caracteristicas
#Filho(Pai) utilizo o sinal de () para herença

class Categoria(models.Model):# a classe é um conjunto de objetos

    # toda classe começa com letra Maiscula(PascalCase)
    nome= models.CharField(max_length=88, null=False, blank=False)

    #max_length: limitr de caracteres
    #null-> nenhuma informação
    #blank:string vazia""

    def __str__(self):
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    nome = models.CharField(max_length=80, null= False,blank=False)

    perfil= models.TextField()

    def __str__(self):
        return  self.nome + self.perfil



class Noticia(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)

    conteudo = models.TextField(null=False, blank=False)

    data_publicacao = models.DateTimeField(null=False, blank=False)

    destaque = models.CharField(
           max_length=2,
           choices=[
               ('0', '0'),
               ('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5')  # <--- MUST BE ADDED TO CHOICES
           ],
           default='5',  # <--- DEFAULT VALUE SET HERE
           null=False,
           blank=False
       )

    foto = models.ImageField(upload_to="fotos/%Y/%m/%d",null=False, blank=False)

    #Relacionamento N-1(Muitas Noticias para um Autor)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias_autor', null=False)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias_categoria', null=False)

    def __str__(self):
        return self.titulo
    
    def is_a_highlight(self):
        # A helper method to check if the rank is within the highlight range (0-5)
        return 0 <= self.priority_rank <= 5 

# Django ORM
# Python e Flask: SQLAlchemy
# Python e Django: Django ORM
# Java: Hibernate
# C#: Entity Framework
# PHP: Doctrine

# vantagem:

"""
    - Usar a linguagem de fluência
    - Migração (migrar de um banco MySQL para um SQLServer)
    - Menos erros (conexão, segurança entre outros)
    - Toolkit extra interação com banco de dados
"""
# desvantagem:

"""
    - Sistemas legados poder ser um problema
    - Iniciantes criar uma ilusão (não precisa estudar SQL)
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# Estudar o que é orm (object relation mapper)

#Herença é uma classe herda de outra classe e implementa suas próprias caracteristicas
#Filho(Pai) utilizo o sinal de () para herença

class Categoria(models.Model):# a classe é um conjunto de objetos

    # toda classe começa com letra Maiscula(PascalCase)
    nome= models.CharField(max_length=88, null=False, blank=False)

    #max_length: limitr de caracteres
    #null-> nenhuma informação
    #blank:string vazia""

    def __str__(self):
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    nome = models.CharField(max_length=80, null= False,blank=False)

    perfil= models.TextField()

    def __str__(self):
        return  self.nome + self.perfil



class Noticia(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)

    conteudo = models.TextField(null=False, blank=False)

    data_publicacao = models.DateTimeField(null=False, blank=False)

    destaque = models.CharField(
           max_length=2,
           choices=[
               ('0', '0'),
               ('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5')  # <--- MUST BE ADDED TO CHOICES
           ],
           default='5',  # <--- DEFAULT VALUE SET HERE
           null=False,
           blank=False
       )

    foto = models.ImageField(upload_to="fotos/%Y/%m/%d",null=False, blank=False)

    #Relacionamento N-1(Muitas Noticias para um Autor)

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias_autor', null=False)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias_categoria', null=False)

    def __str__(self):
        return self.titulo
    
    def is_a_highlight(self):
        # A helper method to check if the rank is within the highlight range (0-5)
        return 0 <= self.priority_rank <= 5 

# Django ORM
# Python e Flask: SQLAlchemy
# Python e Django: Django ORM
# Java: Hibernate
# C#: Entity Framework
# PHP: Doctrine

# vantagem:

"""
    - Usar a linguagem de fluência
    - Migração (migrar de um banco MySQL para um SQLServer)
    - Menos erros (conexão, segurança entre outros)
    - Toolkit extra interação com banco de dados
"""
# desvantagem:

"""
    - Sistemas legados poder ser um problema
    - Iniciantes criar uma ilusão (não precisa estudar SQL)
"""
