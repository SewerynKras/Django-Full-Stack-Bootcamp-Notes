from django.shortcuts import render

# Create your views here.


def helppage(request):
    context = {"help_message": "You need help, dont you"}
    return render(request, "helppage/index.html", context=context)
