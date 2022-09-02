from .models import Sms
from django.forms import ModelForm, TextInput, Textarea


class SmsForm(ModelForm):
    class Meta:
        model = Sms
        fields = ["title", "sms"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            "sms": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text'
            }),
        }