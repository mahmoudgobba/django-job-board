from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserCreateForm(UserCreationForm):
    class Meta():
        fields = ('username','email','password1','password2')
        model = User

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('city','phone_number','image')
