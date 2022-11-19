from http.client import HTTPResponse
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home de solicitud de crédito')

def health(request):
    return HttpResponse('OK')