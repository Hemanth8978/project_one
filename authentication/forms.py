from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','gender','date_of_birth','email','phone','username']
        widgets={
                'gender':forms.RadioSelect(),
                'date_of_birth':forms.DateInput(attrs={'type':'date'})
        }
        labels={
            'date_of_birth':'Date of Birth',
        }

class IdentifyUserForm(forms.Form):
    username_or_email=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'enter the email or userename'}))
class OTPform(forms.Form):
    enter_otp=forms.IntegerField()