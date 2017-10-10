from django import forms

from .models import Post
<<<<<<< HEAD
from .models import Consulta
=======
>>>>>>> 3dc1fb21c8ebb663bac49ad2a7efbe2c54ac7f47

class PostForm(forms.ModelForm):
    
    class Meta:
<<<<<<< HEAD
        #model = Post
        #fields = ('title', 'text', 'author')
        
        model = Consulta
        fields = ('estado', 'data_inicio', 'data_fim')
        widgets={
            "estado":forms.Select(attrs={'class':'form-control'}),
            "data_inicio":forms.TextInput(attrs={'type':'date','class':'form-control'}),
            "data_fim":forms.TextInput(attrs={'type':'date','class':'form-control'}),
        }  
=======
        model = Post
        fields = ('title', 'text')
>>>>>>> 3dc1fb21c8ebb663bac49ad2a7efbe2c54ac7f47
