from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # verifica usuario
    if request.method == 'POST':
        usuario = request.POST['username']
        contrasena = request.POST['password']
        # autenticar
        user = authenticate(request,
                            username=usuario,
                            password=contrasena)
        
        if user is not None:
            login(request,user)
            messages.success(request,'Bienvenido... ')
            return redirect('home')
        else:
            messages.error(request,'Usuario o contraseña incorrecta.')
            return redirect('home')

    return render(request,'home.html',{})

# def login_user(request):
#     pass

# def logout_user(request):
#     pass