from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                "Bienvenido",
                "Gracias por registrarte.",
                "tuemail@gmail.com",
                [user.email],
                fail_silently=False,
            )
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "cuentas/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
