from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "이메일을 써주세요",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )