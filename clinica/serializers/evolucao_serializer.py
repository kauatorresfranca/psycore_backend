from rest_framework import serializers
from ..models.evolucao import Evolucao

class EvolucaoSerializer(serializers.ModelSerializer):
    """
    Tradutor para a Evolução Clínica.
    Garante que cada evolução esteja amarrada a uma sessão.
    """
    class Meta:
        model = Evolucao
        fields = '__all__'
        read_only_fields = ['id', 'data_criacao']

    # Exemplo de validação: Impede criar evolução sem texto
    def validate_descricao(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "A evolução está muito curta. Descreva melhor a sessão."
            )
        return value