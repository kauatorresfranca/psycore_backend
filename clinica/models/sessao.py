from django.db import models

class Sessao(models.Model):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    data_hora = models.DateTimeField() 
    duracao = models.IntegerField(default=50)  
    
    def __str__(self):
        return f"Sessão de {self.paciente.nome} em {self.data_hora}"