from django.shortcuts import HttpResponse, render


def home_page(request):
    context = {
        "title": "Hello World!",
    }
    return render(request, "ecommerce/home_page.html", context)


def about_page(request):
    context = {
        "title": "About",
    }
    return render(request, "ecommerce/about_page.html", context)


def contact_page(request):
    context = {
        "title": "Contact",
    }
    if request.method == "POST":
        print("A post request has been made!", request.POST.get('fullName'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
