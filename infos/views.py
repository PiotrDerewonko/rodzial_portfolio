from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
    t = loader.get_template("infos/main.html")
    c = {"test": "dodawanie", 'title': 'Homepage'}
    return HttpResponse(t.render(c))

def about_me(request):
    t = loader.get_template("infos/about_me.html")
    c = {'title': 'O mnie'}
    return HttpResponse(t.render(c))

def contact(request):
    t = loader.get_template("infos/contact.html")
    c = {'title': 'Kontakt'}
    return HttpResponse(t.render(c))
