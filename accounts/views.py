from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

from django import forms
from accounts.models import CustomUser


class EmailLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def post(self, request):
        user = authenticate(request, email=request.POST["email"],
                            password=request.POST["password"])
        if user:
            login(request, user)
            messages.success(request, 'Başarıyla Giriş Yapıldı')
            return redirect('/')
        else:
            messages.error(request, 'Giriş Başarısız')
        return render(request, 'login.html', {'error': 'Hatalı şifre ya da eposta.'})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget = forms.EmailInput(
            attrs={'autofocus': True, 'placeholder': 'E-mail', 'type': 'email'})
        form.fields['username'].label = 'E-mail'
        return form


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Şifreler uyuşmuyor')
            return render(request, 'register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email zaten kayıtlı')
            return render(request, 'register.html')

        user = CustomUser.objects.create_user(email=email, password=password, name=name, surname=surname)
        user.save()

        login(request, user)
        return redirect('/')
    else:
        return render(request, 'register.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yapıldı')
    return redirect('/')