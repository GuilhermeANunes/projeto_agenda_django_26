from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso.')
            return redirect('contact:index')

    return render (
            request,
            'contact/register.html',
            context= {
                'form': form,
            }
        )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect('contact:index')
        messages.error(request, 'Login inválido.')

    return render (
            request,
            'contact/login.html',
            context= {
                'form': form,
            }
        )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Desconectado com sucesso.')
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render (
                request,
                'contact/register.html',
                context= {
                    'form': form,
                }
            )
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuario atualizado com sucesso.')
        return redirect('contact:index')

    messages.error(request, 'Não foi possível atualizar o usuario.')

    return render (
                request,
                'contact/register.html',
                context= {
                    'form': form,
                }
            )
