from django import forms
from .models import Movie

# define the class of a form

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = {'title' : '','video' : ''}