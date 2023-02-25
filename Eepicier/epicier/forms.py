from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['firstName','lastName','age','phone','email']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre prénom'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom de famille'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre age'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre Téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
        }
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ['title','price','description','category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le titre du produit'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la description du produit'}),
            'category': forms.Select(attrs={'class':'custom-select'}),
        }

class CreditForm(ModelForm):
    class Meta:
        model = Credit
        fields = ['client','produit']
        widgets= {
            'client': forms.Select(attrs={'class':'custom-select'}),
            'produit': forms.Select(attrs={'class':'custom-select'}),
        }

class CreditUpdate(ModelForm):
    class Meta:
        model = Credit
        fields = ['status']
        widgets= {
            'status': forms.Select(attrs={'class':'custom-select mt-2 text-center'}),
        }
        

class CreateNewUser(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','style':'min-width:75vw', 'placeholder': 'Entrez votre username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }