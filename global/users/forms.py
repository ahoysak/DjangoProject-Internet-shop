from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input__form_register'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input__form_register'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input__form_register'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input__form_register'}))
    phone_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input__form_register'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'input__form_register'} ))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'input__form_register'}))



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username' ,'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

#        self.fields['username'].widget.attrs['class'] = 'input__form_register'
#        self.fields['password1'].widget.attrs['class'] = 'input__form_register'
#        self.fields['password2'].widget.attrs['class'] = 'input__form_register'