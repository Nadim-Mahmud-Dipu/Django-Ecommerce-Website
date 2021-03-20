from django.shortcuts import HttpResponse, render, redirect
from django.utils.http import is_safe_url

from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "This is some content",
    }

    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHH!!!!!!"

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


# def login_page(request):
#     login_form = LoginForm(request.POST or None)
#     context = {
#         "form" : login_form
#     }
#     print(request.user.is_authenticated)
#     if login_form.is_valid():
#         print(login_form.cleaned_data)
#         username = login_form.cleaned_data.get("username")
#         password = login_form.cleaned_data.get("password")
#         user = authenticate(request,username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             return redirect("login/")
#         else:
#             print("Error")
#
#     return render(request,"auth/login.html",context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form,
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")

        new_user = User.objects.create_user(username, email, password)
        #new_user.save()
        print(new_user)

    return render(request, "auth/register.html", context)
