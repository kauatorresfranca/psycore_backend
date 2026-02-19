from rest_framework import serializers
from ..models.sessao import Sessao

class SessaoSerializer(serializers.ModelSerializer):
    """
    Tradutor para as Sessões. 
    Incluímos o nome do paciente para facilitar a visualização na agenda.
    """
    # Campo extra que busca o nome através da FK do paciente
    paciente_nome = serializers.ReadOnlyField(source='paciente.nome')

    class Meta:
        model = Sessao
        fields = [
            'id', 'paciente', 'paciente_nome', 
            'data_hora', 'duracao'
        ]
        read_only_fields = ['id']