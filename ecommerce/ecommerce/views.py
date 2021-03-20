from django.shortcuts import HttpResponse, render

def home_page(request):
    return HttpResponse("<h1> Hello World!</h1>")