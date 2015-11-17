from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.http import JsonResponse
from main.models import Movie, MovieCas
# Create your views here.

import string


def movie_list_cas(request):

    context = {}

    movie_list = MovieCas.objects.all()

    context['movie_list'] = movie_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))


def movie_list_temp(request):

    context = {}

    movie_list = Movie.objects.all()[:50000]

    context['movie_list'] = movie_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))


def movie_list_mysql(request):

    context = {}

    movie_list = Movie.objects.using('mysql').all()[:50000]

    context['movie_list'] = movie_list

    return render_to_response('movie_list.html', context, context_instance=RequestContext(request))


def movie_list(request):

    movies = Movie.objects.all()[:100]

    api_dict = {}

    movie_list = []

    api_dict['movies'] = movie_list

    for movie in movies:
        movie_list.append({
            'title': movie.dvd_title,
            'studio': movie.studio,
            'status': movie.status,
            'price': movie.price,
            'rating': movie.rating,
            'genre': movie.genre,
            'release': movie.dvd_release_date,
            })
    return JsonResponse(api_dict)
