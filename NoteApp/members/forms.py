from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-title', 'placeholder':'email'})),
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-title', 'placeholder':'firstname'})),
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-title', 'placeholder':'lastname'})),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')
        

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['class'] ='form-title', 
            self.fields['password1'].widget.attrs['class']='form-title',
            self.fields['password2'].widget.attrs['class']='form-title', 
             