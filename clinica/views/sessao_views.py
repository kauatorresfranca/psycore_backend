from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.sessao import Sessao
from ..serializers import SessaoSerializer

# 1. Rota para Listar e Criar (Coleção)
@api_view(['GET', 'POST'])
def sessao_list_create(request):
    if request.method == 'GET':
        # Filtro opcional por data (que sua Agenda usa)
        data_query = request.query_params.get('data')
        if data_query:
            sessoes = Sessao.objects.filter(data=data_query)
        else:
            sessoes = Sessao.objects.all()
            
        serializer = SessaoSerializer(sessoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SessaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Rota para Detalhes e Atualização (Instância única)
@api_view(['GET', 'PATCH', 'DELETE'])
def sessao_detail(request, pk):
    sessao = get_object_or_404(Sessao, pk=pk)

    if request.method == 'GET':
        serializer = SessaoSerializer(sessao)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # O partial=True é o que permite o PATCH funcionar só com 1 campo
        serializer = SessaoSerializer(sessao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sessao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)