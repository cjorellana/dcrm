from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    # obtiene los record
    records = Record.objects.all()

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
            messages.info(request,'Bienvenido... ')
            return redirect('home')
        else:
            messages.error(request,'Usuario o contraseña incorrecta.')
            return redirect('home')

    return render(request,'home.html',{'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.warning(request,'Adios ... ')
    return redirect('home')


def register_user(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,'Bienvenido ... ')
            return redirect('home')
    else:
        form = SignUpForm()
        context = {'form':form}
        return render(request,'register.html',context) 

    return render(request,'register.html',{'form':form})

def select_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk)
        return render(request,'record.html',{'record':record})
    else:
        messages.success(request,'Identificate primero ... ')
        return redirect('home')