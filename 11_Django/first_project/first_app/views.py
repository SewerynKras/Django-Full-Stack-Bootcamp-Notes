from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, User
from first_app.forms import NewUserForm
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
    context = {"form": NewUserForm()}

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            # add the new user to the list
            form.save(commit=True)
            # return him to the users list
            return users(request)

    return render(request, "first_app/form_page.html", context=context)


def users(request):
    users_list = User.objects.all()
    context = {"users_list": users_list}
    return render(request, "first_app/users.html", context=context)
