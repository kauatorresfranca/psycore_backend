from rest_framework import serializers
from ..models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paciente
        fields = '__all__' # Expõe todos os campos do model no JSON
        read_only_fields = ['id', 'data_cadastro']