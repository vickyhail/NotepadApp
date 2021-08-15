#from django.db.models import fields
#from django.forms import widgets
from .models import Note
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'Description', 'body')

        widgets = {

           'title': forms.TextInput(attrs={'class':'form-title', 'placeholder':'title'}),
           'Description': forms.TextInput(attrs={'class':'form-description', 'placeholder':'Description'}),
           'body': forms.Textarea(attrs={'class':'form-textarea', 'placeholder':'Body'}),
           


        }
