from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("YOU ARE IN THE INDEX FILE")
def hello(request):
    return HttpResponse("THIS IS ANOTHER MESSAGE")
def list_clients(request):
    return HttpResponse("HERE YOU MUST LIST THE CLIENTES IN DB")

# Create your views here.
