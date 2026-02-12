from django.db import models

class Evolucao(models.Model):
    # Uma evolução pertence a uma sessão específica
    sessao = models.OneToOneField('Sessao', on_delete=models.CASCADE)
    # Mantemos o paciente aqui também para facilitar buscas rápidas (filtros)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)