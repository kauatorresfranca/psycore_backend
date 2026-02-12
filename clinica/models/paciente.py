from django.db import models

STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('alta', 'Teve Alta'),
    ]

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_telefone = models.CharField(max_length=20)
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='ativo'
    )
    data_nascimento = models.DateField()
    contato_emergencia = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome