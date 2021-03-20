from django.shortcuts import HttpResponse, render
from .forms import ContactForm


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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    if request.method == "POST":
        print("A post request has been made!", request.POST.get('fullName'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)
