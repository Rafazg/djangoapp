from django import forms
from .models import Livros

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