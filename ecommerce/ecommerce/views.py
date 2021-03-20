from django.shortcuts import HttpResponse, render


def home_page(request):
    return render(request, "ecommerce/home_page.html")

def about_page(request):
    return render(request, "ecommerce/about_page.html")

def contact_page(request):
    return render(request, "ecommerce/contact_page.html")
