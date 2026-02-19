from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.sessao import Sessao
from ..serializers import SessaoSerializer

@api_view(['GET', 'POST'])
def sessao_list_create(request):
    if request.method == 'GET':
        sessoes = Sessao.objects.all()
        serializer = SessaoSerializer(sessoes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SessaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)