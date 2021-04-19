from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json
import importlib


# Create your views here.
def index(request):
    return HttpResponse('Hello World, Welcome to CovidStatsChile')