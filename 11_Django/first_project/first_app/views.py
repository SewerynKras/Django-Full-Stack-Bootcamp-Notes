from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello there<h1>")


def nested(request):
    context = {"insert_me": "Ah welcome from views.py"}
    return render(request, "first_app/index.html", context=context)


def image(request):
    return render(request, "first_app/pic.html")


def webpages(request):
    webpages = Webpage.objects.order_by("name")
    context = {"webpages": webpages}
    return render(request, "first_app/webpages.html", context=context)
