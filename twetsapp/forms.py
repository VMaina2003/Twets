from django import forms
from .models import Twet

class TwetForm(forms.ModelForm):
    class Meta:
        model = Twet
        fields = ['content', 'description', 'image']
