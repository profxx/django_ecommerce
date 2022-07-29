from django.http import HttpResponse
from django.shortcuts import render
from template import index.html

def homepage(request):


    return render(request, "index.html", {})