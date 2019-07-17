from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello there<h1>")


def nested(request):
    context = {"insert_me": "Ah welcome from views.py"}
    return render(request, "first_app/index.html", context=context)