from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json
import importlib
import pandas as pd
import csv


# Create your views here.
def index(request):
    return HttpResponse('Hello World, Welcome to CovidStatsChile')

# Función que se encarga de captar la información de las comunas
def get_communes_info(request):
    jsonArray=[]
    with requests.Session() as s:
        download = s.get("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/Otros/InformacionComunas.csv")

        decoded_content = download.content.decode('utf-8')

    lines = decoded_content.splitlines()
    reader = csv.reader(lines)
    data = list(reader)
    print(data)
    all_communes = [dict(zip(data[0], row)) for row in data[1:] if row[1]=="13"]
    print(all_communes)
    # Traspasamos la respuesta a la vista
    return render(request, 'stats/communes-info.html', {"all_communes": all_communes})
