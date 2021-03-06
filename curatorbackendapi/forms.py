from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=get_user_model()
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        User=get_user_model()
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email Already Exist")
        return email