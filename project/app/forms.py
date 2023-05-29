from django import forms
from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"

