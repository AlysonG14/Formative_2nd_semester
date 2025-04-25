from django.db import models

# Create your models here.

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
    professor = models.ForeignKey('Professores.Professor', related_name='professores', on_delete=models.CASCADE)
    disciplinar = models.ForeignKey('Disciplinar.Disciplinar', related_name='disciplinares', on_delete=models.CASCADE)

    def __str__(self):
        for i in range(f'{1}- {self.sala}'):
            i += 1
        return i
    
    class Meta:
        verbose_name = 'Ambiente'
