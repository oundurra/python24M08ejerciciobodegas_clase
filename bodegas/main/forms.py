from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import TipoBodega, Bodega

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obligatorio')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TipoBodegaForm(forms.Form):
    tipo_bodega = forms.ModelChoiceField(queryset=TipoBodega.objects.all(), required=True)

    class Meta:
        model = TipoBodega
        fields = ['id']

    def __init__(self, *args, **kwargs):   
        super(TipoBodegaForm, self).__init__(*args, **kwargs)

class BodegaForm(forms.Form):
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.all(), required=True)