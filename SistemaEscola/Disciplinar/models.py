from django.db import models

# Create your models here.

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
    professor = models.ForeignKey('Professores.Professor', related_name='disciplinas', on_delete=models.CASCADE) # Usando o modelo CASCADE

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Disciplinare'

