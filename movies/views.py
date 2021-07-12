from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Movie
from django.contrib import messages
from .movie_form import MovieForm

# Create your views here.

# Using FBV here. We could use Listviews and make this CBV as well. However, for simplicity, using CBV.

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html', {"title":"Home", "movies":movies})

def search(request):
    if request.method == "POST":
        movies = Movie.objects.filter(name__contains=request.POST['movie'])
        return render(request, 'movies/home.html', {"title":"Search results", "movies":movies})
    else:
        search_str = request.GET.get('q', None)
        if search_str == None:
            return JsonResponse('', safe=False)
        movies = Movie.objects.filter(name__contains=search_str).values()
        movies_json = list(movies)
        return JsonResponse(movies_json, safe=False)

def create(request):
    if request.method == "POST":
        m_form = MovieForm(request.POST)
        if m_form.is_valid():
            m_instance = m_form.save(commit=False)
            messages.success(request, f'New product created!')
            m_instance.save()
            return redirect('movies-home')
    else:
        m_form = MovieForm()
    return render(request, 'movies/create_new.html', {'form':m_form})
