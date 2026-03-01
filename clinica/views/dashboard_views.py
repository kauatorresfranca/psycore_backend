from rest_framework.decorators import api_view
from rest_framework.response import Response

from clinica.models import sessao
from ..models.paciente import Paciente

@api_view(['GET'])
def dashboard_view(request):
    # Captura as duas datas. Se não vierem, podemos definir um padrão (ex: os últimos 7 dias)
    data_inicio = request.query_params.get('inicio')
    data_fim = request.query_params.get('fim')

    # Base da query
    agendamentos = sessao.objects.all()

    # Aplica os filtros apenas se as datas forem enviadas
    if data_inicio and data_fim:
        agendamentos = agendamentos.filter(
            data__gte=data_inicio, 
            data__lte=data_fim
        )

    return Response({
        "total_no_periodo": agendamentos.count(),
        "agenda": [
            {"data": a.data, "hora": a.hora, "paciente": a.paciente.nome} 
            for a in agendamentos.order_by('data', 'hora')
        ]
    })