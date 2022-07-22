from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
from .forms import MovieForm
from .models import Movie

import random

def index(request):
    """Returns to the Homepage"""
    return render(request, "movies/index.html")

def new_movie(request):
    """Handles new movie uploads"""
    if request.method != "POST":
        form = MovieForm()
    else:
        form = MovieForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect("movies:all_movies")
    
    context = {"form" : form}
    return render(request, "movies/new_movie.html", context)

def all_movies(request):
    """Handles new movie uploads"""
    movies = Movie.objects.all()

    movie = random.choice(movies)

    context = {"movies" : movies, "movie" : movie}
    return render(request, "movies/movies.html", context)

def view_movie(request, movie_id):
    """Handles new movie uploads"""
    movie = Movie.objects.get(id=movie_id)
    
    context = {"movie" : movie}
    return render(request, "movies/view_movie.html", context)