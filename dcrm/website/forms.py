from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", 
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Correo'}))
    first_name = forms.CharField(label="", max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Nombre'}
        ))
    last_name = forms.CharField(label="", max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Apellido'}
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].label = ""
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_.</small></span>'

        mesaje = '<ul class="form-text text-muted small">' \
            '<li>Su contraseña no puede ser demasiado similar a su otra información personal.</li>' \
            '<li>Su contraseña debe contener al menos 8 caracteres.</li>' \
            '<li>Su contraseña no puede ser una contraseña de uso común.</li>' \
            '<li>Su contraseña no puede ser completamente numérica.</li></ul>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = mesaje


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña que antes, para verificación.</small></span>'	

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Nombre'}
        ),label="")
    
    last_name = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Apellido'}
        ),label="")
    
    email = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Correo Electronico'}
        ),label="")
    
    phone = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Telefono'}
        ),label="")
    
    address = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Dirección'}
        ),label="")
    
    city = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Ciudad'}
        ),label="")
    
    state = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Departamento'}
        ),label="")
    
    zipcode = forms.CharField(required=True, max_length=100,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder': 'Zip Code'}
        ),label="")

    class Meta:
        model = Record
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
         super(AddRecordForm, self).__init__(*args, **kwargs)

    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['name'].widget.attrs['placeholder'] = 'Nombre'
    #     self.fields['name'].label = ""
         self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Requerido. 20 caracteres o menos. </small></span>'