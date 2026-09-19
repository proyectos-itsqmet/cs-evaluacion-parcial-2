from django.forms import ModelForm
from .models import Perro

class PerroForm(ModelForm):
    class Meta:
        model = Perro
        fields = "__all__"
