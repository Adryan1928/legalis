from django.shortcuts import render, redirect
from .forms import ClientForm, UserForm
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User

def landingPage(request):
    return render(request, 'landingPage.html')

def register(request):
    
    context = {
        'form_client': ClientForm(),
        'form_user': UserForm(),
        'height': 'h-auto',
    }

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST, request.FILES)

        context['form_client'] = client_form
        context['form_user'] = user_form

        user = User.objects.filter(email=user_form.data.get('email')).first()

        if (user_form.data.get('password') != user_form.data.get('password2')):
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')

            return render(request, 'registration/register.html', context)
        
        elif (str(user_form.data.get('email')) == ''):
            messages.add_message(request, constants.ERROR, 'O email não pode ser vazio')

            return render(request, 'registration/register.html', context)
        elif (user):
            messages.add_message(request, constants.ERROR, 'Email já cadastrado')

            return render(request, 'registration/register.html', context)

        if user_form.is_valid() and client_form.is_valid():
            user = User.objects.create_user(**user_form.cleaned_data, username=user_form.cleaned_data['email'])
            client = client_form.save(commit=False)
            print(client.profile_photo)
            client.user = user
            client.save()

            return redirect('user:login')
        else:
            for error in user_form.errors.keys():
                if (error == 'email'):
                    messages.add_message(request, constants.ERROR, 'Email inválido')
                elif (error == 'password'):
                    messages.add_message(request, constants.ERROR, 'Senha inválida')
                elif (error == 'first_name'):
                    messages.add_message(request, constants.ERROR, 'Nome inválido')

    return render(request, 'registration/register.html', context)