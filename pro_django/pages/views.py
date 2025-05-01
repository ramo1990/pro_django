from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    list = [3,4,5,7,8,8]
    user = request.user
    context = {
        "list":list,
        "user" : user
    }

    """if user.is_authenticated:
        context['user'] = user.username
    else:
        context['user'] = "User non connecté"""

    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1> About page </h1>")
    return render(request, "about.html")

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Contact page </h1>")
    return render(request, "contact.html")