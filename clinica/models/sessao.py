from django.db import models

STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

class Sessao(models.Model):

    class Meta:
        ordering = ['data', 'hora'] # Organiza da mais antiga para a mais nova

    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='sessoes')
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    evolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} às {self.hora}"