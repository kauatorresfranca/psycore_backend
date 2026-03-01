from rest_framework import serializers
from ..models.sessao import Sessao

class SessaoSerializer(serializers.ModelSerializer):
    paciente_nome = serializers.ReadOnlyField(source='paciente.nome')

    class Meta:
        model = Sessao
        fields = [
            'id', 'paciente', 'paciente_nome', 'data', 
            'hora', 'status', 'evolucao'
        ]
        read_only_fields = ['id']