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


    def __str__(self):
        return f'{self.ni}- {self.nome}'
    
    class Meta:
        verbose_name = 'Professore'

CURSO = [
    ('MC', 'Mecatrônica'),
    ('ADM', 'Administração'),
    ('ADS', 'Análise e Desenvolvimento de Sistemas'),
    ('MA', 'Manufatura'),

]

class Disciplinar(models.Model):
    nome = models.CharField(max_length= 255, blank=True, null=True)
    curso = models.CharField(max_length= 3, choices=CURSO, blank=True, null=True)
    carga_horaria = models.TimeField(blank=True, null=True)
    descricao = models.CharField(max_length= 255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Disciplina'

PERIODO = [
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite')
]

class Ambiente(models.Model):
    data_inicio = models.DateTimeField()
    data_termino = models.DateTimeField()
    periodo = models.CharField(max_length=5, choices=PERIODO)
    sala = models.CharField(max_length=255)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinar, on_delete=models.CASCADE)

    def __str__(self):
        return(self.sala)
    
    class Meta:
        verbose_name = 'Ambiente'
