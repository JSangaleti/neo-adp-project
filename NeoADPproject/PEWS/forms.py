from django import forms
from .models import profissional_de_saude


class LoginForm:
    username = forms.CharField(label="CPF")
    password = forms.PasswordInput()
    model = profissional_de_saude
    fields = ["cpf", "senha"]
