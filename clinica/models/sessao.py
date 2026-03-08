from django.db import models

STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('confirmado', 'Confirmado'),
    ('cancelado', 'Cancelado'),
]

class Sessao(models.Model):
    class Meta:
        ordering = ['data', 'hora']

    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name='sessoes')
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    tipo_consulta = models.CharField(max_length=100, default='Fisioterapia') # Adicionado para o Front
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # Adicionado para o Faturamento
    evolucao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} às {self.hora}"