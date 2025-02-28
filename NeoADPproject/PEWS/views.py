from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import profissional_de_saude


# Create your views here.
def index(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        senha = request.POST.get("senha")

        pds = profissional_de_saude.objects.get(cpf=cpf)

        if pds.senha == senha:
            login(request, pds)
            return redirect("pews")
        else:
            return render(request, "login.html", {"erro": "CPF ou senha inválidos"})
    return render(request, "login.html")


@login_required
def protegida(request):
    return render(request, "meuapp/protegida.html")


@login_required
def pews(request):
    return render(request, "index.html")
