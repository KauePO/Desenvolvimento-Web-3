from django.shortcuts import render
from datetime import datetime

def natal(request):
    contexto = {'natal': False}
    data = datetime.now()
    data = str(data.strftime("%m-%d"))

    if (data == "12-25"):
        contexto = {'natal': True}

    return render(request, 'natal.html', contexto)
