from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.evolucao import Evolucao
from ..serializers import EvolucaoSerializer

@api_view(['GET', 'POST'])
def evolucao_list_create(request):
    if request.method == 'GET':
        evolucoes = Evolucao.objects.all()
        serializer = EvolucaoSerializer(evolucoes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EvolucaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)