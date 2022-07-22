from django import forms
from .models import Movie

from moviepy.editor import VideoFileClip

# define the class of a form

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = {'title' : '','video' : ''}

     # Add some custom validation to our image field