from django.db import models



class User(models.Model):
    pass

class Employee(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    office = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    start_date = models.DateField()
    salary = models.PositiveIntegerField()


    def __str__(self):
        return self.name
    pass


class Livros(models.Model):
    nome_do_autor = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    
    nome_da_obra = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    categoria = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    
    data_de_registro = models.DateField(
        default=0,
        null=False,
        blank=False
    )
    
    
    def __str__(self):
        return self.nome_do_autor
    pass