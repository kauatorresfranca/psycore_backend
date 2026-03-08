from datetime import date
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from clinica.models.sessao import Sessao
from ..models.paciente import Paciente

@api_view(['GET'])
def dashboard_view(request):
    data_inicio = request.query_params.get('inicio')
    data_fim = request.query_params.get('fim')
    hoje = date.today()

    # Querysets
    todos_pacientes = Paciente.objects.all()
    sessoes_periodo = Sessao.objects.all()

    if data_inicio and data_fim:
        sessoes_periodo = sessoes_periodo.filter(data__gte=data_inicio, data__lte=data_fim)

    # Cálculos
    pacientes_count = todos_pacientes.count()
    consultas_hoje = Sessao.objects.filter(data=hoje).count()
    
    # Evoluções pendentes: sessões passadas sem texto de evolução
    evolucoes_pendentes = Sessao.objects.filter(
        data__lt=hoje, 
        evolucao__in=['', None]
    ).exclude(status='cancelado').count()

    # Faturamento real (Soma do campo valor no período selecionado)
    faturamento_total = sessoes_periodo.aggregate(total=Sum('valor'))['total'] or 0

    # Agenda formatada para o Front-end
    agenda_data = []
    for s in sessoes_periodo.order_by('data', 'hora')[:10]:
        agenda_data.append({
            "id": s.id,
            "paciente": s.paciente.nome,
            "horario": f"{s.data.strftime('%d/%m')} - {s.hora.strftime('%H:%M')}",
            "tipoConsulta": s.tipo_consulta
        })

    return Response({
        "pacientes": pacientes_count,
        "consultasHoje": consultas_hoje,
        "evolucoesPendentes": evolucoes_pendentes,
        "faturamento": float(faturamento_total),
        "agenda": agenda_data
    })