from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel

def natal(request):
    feriado_no_banco = FeriadoModel.objects.all()
    contexto = {'feriado': None}


    data = datetime.now()
    dia = data.strftime("%d")
    mes = data.strftime("%m")

    dia_int = int(dia)
    mes_int = int(mes)


    for feriado in feriado_no_banco:
        if (feriado.mes == mes_int and feriado.dia == dia_int): 
            contexto['feriado'] = feriado.nome

    if contexto['feriado'] is None:
        contexto['feriado'] = "não é feriado"


    #import ipdb; ipdb.set_trace()
    return render(request, 'natal.html', contexto)
