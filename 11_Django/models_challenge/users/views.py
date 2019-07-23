from django.shortcuts import render
from users.models import User


# Create your views here.
def ViewUsers(request):
    users = User.objects.order_by("first_name")
    context = {"users_list": users}
    return render(request, "users/index.html", context=context)
