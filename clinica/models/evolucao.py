from django.db import models

class Evolucao(models.Model):
    sessao = models.OneToOneField('Sessao', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)