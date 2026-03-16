from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.sessao import Sessao
from ..serializers import SessaoSerializer

# 1. Rota para Listar e Criar (Coleção)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sessao_list_create(request):
    if request.method == 'GET':
        data_query = request.query_params.get('data')
        # Filtra apenas as sessões da psicóloga logada
        sessoes_base = Sessao.objects.filter(usuario=request.user)
        
        if data_query:
            sessoes = sessoes_base.filter(data=data_query)
        else:
            sessoes = sessoes_base.all()
            
        serializer = SessaoSerializer(sessoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SessaoSerializer(data=request.data)
        if serializer.is_valid():
            # Salva a sessão atrelando-a à psicóloga logada
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Rota para Detalhes e Atualização (Instância única)
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def sessao_detail(request, pk):
    # O filtro usuario=request.user impede que uma psicóloga acesse o ID de outra
    sessao = get_object_or_404(Sessao, pk=pk, usuario=request.user)

    if request.method == 'GET':
        serializer = SessaoSerializer(sessao)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = SessaoSerializer(sessao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sessao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)