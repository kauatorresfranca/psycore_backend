from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..models.paciente import Paciente
from ..serializers import PacienteSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def paciente_list_create(request):
    if request.method == 'GET':
        # Retorna apenas os pacientes da psicóloga logada
        pacientes = Paciente.objects.filter(usuario=request.user)
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            # Salva o paciente atrelando-o automaticamente à psicóloga logada
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)