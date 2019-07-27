from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Webpage, ExtendedUser
from first_app.forms import NewUserForm, ExtendedUserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

    registered = False

    if request.method == "POST":
        user_form = NewUserForm(request.POST)
        extra_form = ExtendedUserForm(request.POST)

        if user_form.is_valid() and extra_form.is_valid():
            # add the new user to the list
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            ext_user = extra_form.save(commit=False)
            ext_user.user = user

            if 'profile_pic' in request.FILES:
                ext_user.profile_pic = request.FILES['profile_pic']

            ext_user.save()

            registered = True

    context = {"user_form": NewUserForm(),
               "extra_form": ExtendedUserForm(),
               "registered": registered}

    return render(request, "first_app/form_page.html", context=context)


def users(request):
    users_list = ExtendedUser.objects.all()
    context = {"users_list": users_list}
    return render(request, "first_app/users.html", context=context)


def login_user(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('home_page'))

    context = {"form": LoginForm()}
    return render(request, "first_app/login.html", context=context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("<h2>Logged out<h2>")
