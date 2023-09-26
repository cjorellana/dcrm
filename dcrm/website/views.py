from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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

def delete_record(request,pk):
    if request.user.is_authenticated:
        record = Record.objects.get(pk=pk)
        record.delete()
        messages.success(request,'Record a sido eliminado ... ')
        return redirect('home')
    else:
        messages.success(request,'Identificate primero ... ')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request,'Record a sido agregado ... ')
                return redirect('home')
        return render(request,'add_record.html',{'form':form})  #get
    else:
        messages.success(request,'Identificate primero ... ')
        return redirect('home')  

def add_record_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            zipcode = request.POST['zipcode']
            country = request.POST['country']
            record = Record(first_name=first_name,last_name=last_name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode,country=country)
            record.save()
            messages.success(request,'Record a sido agregado ... ')
            return redirect('home')
    else:
        messages.success(request,'Identificate primero ... ')
        return redirect('home')

# if form.is_valid():
#     record = YourModelName(
#         field1=form.cleaned_data['field1'],
#         field2=form.cleaned_data['field2'],
#         # ... otros campos
#     )
#     record.save()
#     messages.success(request, 'Record ha sido agregado ...')
#     return redirect('home')