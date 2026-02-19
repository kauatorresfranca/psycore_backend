from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.paciente import Paciente
from ..serializers import PacienteSerializer

@api_view(['GET', 'POST'])
def paciente_list_create(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)