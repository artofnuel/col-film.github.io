from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .decorators import student_only

# Create your views here.
from .forms import MovieForm, MovieCommentForm
from .models import Movie, MovieComment
from django.http import Http404

#Check that the topic owner is the one requesting
def  check_comment_owner(author, user):
    if author != user:
        raise Http404

def index(request):
    """Returns to the Homepage"""
    return render(request, "movies/index.html")

@login_required
@student_only
def new_movie(request):
    """Handles new movie uploads"""

    if request.method != "POST":
        form = MovieForm()
    else:
        form = MovieForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_vid = form.save(commit=False)
            new_vid.author = request.user
            new_vid.save()
        return redirect("movies:all_movies")
    
    context = {"form" : form}
    return render(request, "movies/new_movie.html", context)

@login_required
def new_comment(request, movie_id):
    """Handles new movie comments"""
    movie = Movie.objects.get(id=movie_id)

    if request.method != "POST":
        form = MovieCommentForm()
    else:
        form = MovieCommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.movie = movie
            new_comment.comment_author = request.user
            new_comment.save()
            return redirect("movies:view_movie", movie_id=movie_id)
               
    context = {"form" : form, "movie" : movie} 
    return render(request, "movies/new_comment.html", context)


@login_required
def edit_comment(request, comment_id):
    """Edit an exisiting comment."""
    comment = MovieComment.objects.get(id=comment_id)
    movie = comment.movie

    #check topic belongs to the current user
    check_comment_owner(comment.comment_author, request.user)

    if request.method != 'POST':
        # Initial request; prefill from with current entry.
        form = MovieCommentForm(instance=comment)
    else:
        # Change the data since its POST request
        form = MovieCommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:view_movie',movie_id=movie.id)

    context = {'movie': movie,'comment': comment, 'form': form}
    return render(request, 'movies/edit_comment.html', context)

def all_movies(request):
    """Handles new movie uploads"""
    # try:
    movies = Movie.objects.all()

    #movie = random.choice(movies)   , "movie" : movie

    context = {"movies" : movies}
    return render(request, "movies/movies.html", context)
    
@login_required
def view_movie(request, movie_id):
    """Handles new movie uploads"""
    movie = Movie.objects.get(id=movie_id)

    comments = movie.moviecomment_set.order_by('-date_added')   
    
    context = {"movie" : movie, "comments" : comments }
    return render(request, "movies/view_movie.html", context)