from django import forms
from .models import Livros
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InsereLivroForm(forms.ModelForm):

    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 20})
    )

    class Meta:
        model = Livros

        # Fields in the form that correspond to the model fields
        fields = [
            'nome_do_autor',
            'nome_da_obra',
            'categoria',
            'data_de_registro',
        ]
        

class RegistrationForm(UserCreationForm):
        email = forms.EmailField(required=True)

        class Meta:
            model = User
            fields = ("username", "email", "password1", "password2")    
