#views.py
from django.http.response import JsonResponse, HttpResponse,HttpResponseServerError
from django.shortcuts import render, redirect
import requests
from .models import Comment
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

api_key = settings.API_KEY



def search(request):
    """
    Perform a search using The Movie Database API.

    Args:
        request: Django HTTP request object.

    Returns:
        Rendered template with search results.
    """
    query = request.GET.get('q')

    if query:
        data=requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={api_key}" f"&include_adult=false&language=en-US&page=1&query={query}")
        if data.ok:
            return render(request, 'home/results.html', {
                "data": data.json(),
                "type": request.GET.get("type"),
                
            })
        else:
            return HttpResponseServerError("Error fetching data from the API")

    return HttpResponse("Please enter a search query")

# It's good practice to keep sensitive information in settings or environment variables
def fetch_movie_details(requests,movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    response = requests.get(url)
    if response.ok:
        data = response.json()
        return HttpResponse(data)
    else:
        print('Error fetching data from the API')
        return HttpResponse('Error Fetching movie details')
  
# movies/views.py

# ... (existing imports)

def index(request):
    query = request.GET.get('q')
    search_data  = []

    if query:
        search_data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={api_key}&include_adult=false&language=en-US&page=1&query={query}")
        if search_data.ok:
            all_movies = search_data.json().get('results', [])
        else:
            all_movies = []
    else:
        trending_data = requests.get(f"https://api.themoviedb.org/3/trending/all/week?api_key={api_key}&language=en-US")
       
        
        if trending_data.ok:
            trending_movies_data = trending_data.json()
            all_movies = trending_movies_data.get('results', [])

        else:
            all_movies = []


    return render(request, 'home/index.html', {'all_movies':all_movies})


def view_tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={api_key}&language=en-US")

    if data.ok and recommendations.ok:
        return render(request, "home/tv_detail.html", {
            "data": data.json(),
            "recommendations": recommendations.json(),
            "type": "tv",
        })
    else:
        return HttpResponse("Error fetching data from the API")

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US")
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={api_key}&language=en-US")

    if data.ok and recommendations.ok:
        return render(request, "home/movie_detail.html", {
            "data": data.json(),
            "recommendations": recommendations.json(),
            "type": "movie",
        })
    else:
        return HttpResponse("Error fetching data from the API")

def view_trendings_results(request):
    type_param = request.GET.get("media_type")
    time_window = request.GET.get("time_window")
    trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type_param}/{time_window}?api_key={api_key}&language=en-US")

    if trendings.ok:
        return JsonResponse(trendings.json(),safe=False)
    else:
        return JsonResponse("Error fetching data from the API")



    
@login_required
def comment_page(request, movie_id):
    if request.method == "POST":
        user = request.user
        comment = request.POST.get("comment")

        if not request.user.is_authenticated:
            user = User.objects.get(id=1)

        Comment(comment=comment, user=user, movie_id=movie_id).save()

        return redirect(f"/movie/{movie_id}/comments/")

    else:
        data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US")
        title = data.json()["title"]

        comments = reversed(Comment.objects.filter(movie_id=movie_id))

        return render(request, "home/comments.html", {
            "title": title,
            "comments": comments,
        })

