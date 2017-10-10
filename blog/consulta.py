from django import forms

from .models import Consulta

class ConsultaForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        fields = ('estado', 'data_inicio', 'data_fim')