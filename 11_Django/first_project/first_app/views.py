from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage
from first_app.forms import BasicForm
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


def form(request):
    context = {"form": BasicForm()}

    if request.method == "POST":
        form = BasicForm(request.POST)

        if form.is_valid():
            print("Validation success!")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, "first_app/form_page.html", context=context)
