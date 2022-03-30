from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader



def InicioPage(request):
    return render(request,"InicioPage.html")




