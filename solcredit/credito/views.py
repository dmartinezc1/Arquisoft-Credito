from django.shortcuts import render
from .logic import credito_logic as cl
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

def creditos_view(request):
    if request.method == 'GET':
        creditos = cl.get_creditos()
        creditosdto=serializers.serialize('json',creditos)
        return HttpResponse(creditosdto, 'application/json')

    if request.method=='POST':
        credito= cl.create_credito(json.loads(request.body))
        creditodto=serializers.serialize('json', [credito,])
        return HttpResponse(creditodto, 'application/json')

def credito_view(request,pk):
    if request.method == 'GET':
        try:
            creditos=cl.get_credito(pk)
            creditosdto=serializers.serialize('json', [creditos,])
            return HttpResponse(creditosdto, 'application/json')
        except:
            creditos = cl.get_creditos()
            creditosdto = serializers.serialize('json', creditos)
            return HttpResponse(creditosdto, 'application/json')


# Create your views here.
