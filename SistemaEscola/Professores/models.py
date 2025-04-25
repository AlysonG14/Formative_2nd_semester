from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Professor(models.Model):
    ni = models.IntegerField(null= True, blank= True)
    nome = models.CharField(max_length= 255, blank=True, null=True)
    email = models.CharField(max_length= 255, blank=True, null=True)
    telefone = models.CharField(max_length= 16, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                                         message='O número tem que ser o formato de: 19 12345-6789')], blank= True, null= True) 
    data_nascimento = models.DateField(blank=True, null=True)
    data_contratacao = models.DateField(blank=True, null=True)
    disciplina = models.ForeignKey("Disciplinar.Disciplinar", related_name='professores', on_delete=models.CASCADE) # Usando o modelo CASCADE -> 

    def __str__(self):
        return f'{self.ni}- {self.nome}'
    
    class Meta:
        verbose_name = 'Professore'