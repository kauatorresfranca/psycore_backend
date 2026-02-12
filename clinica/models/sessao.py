from django.db import models

class Sessao(models.Model):
    # Relacionamento com Paciente (1 paciente : N sessões)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    data_hora = models.DateTimeField() # Vital para a agenda
    duracao = models.IntegerField(default=50) # Tempo padrão de sessão de psico
    
    def __str__(self):
        return f"Sessão de {self.paciente.nome} em {self.data_hora}"