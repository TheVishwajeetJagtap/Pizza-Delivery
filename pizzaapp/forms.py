from  django import forms
from .models import PizzaModel

class PizzaModelForm(forms.ModelForm):
    class Meta:
        model=PizzaModel
        fields='__all__'
