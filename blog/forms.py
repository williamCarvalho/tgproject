from django import forms

from .models import Post
from .models import Consulta

class PostForm(forms.ModelForm):
    
    class Meta:
        #model = Post
        #fields = ('title', 'text', 'author')
        
        model = Consulta
        fields = ('estado', 'data_inicio', 'data_fim')
        widgets={
            "estado":forms.Select(attrs={'class':'form-control'}),
            "data_inicio":forms.TextInput(attrs={'type':'date','class':'form-control'}),
            "data_fim":forms.TextInput(attrs={'type':'date','class':'form-control'}),
        }  