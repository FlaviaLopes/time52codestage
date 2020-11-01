from django.shortcuts import render, redirect, HttpResponse
from app.settings import *
from bottle import route, run, request
from spotipy import oauth2

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE,
                               cache_path=CACHE)


# Create your views here.
def index(request):
    #verificar se está logado
    #senão aparece tela login autorização
    #se sim autoriza e vai pra tela 2 de resultados
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/base.html')


def app(request):
    #aqui captura, formata e retorna p apresentação
    #os dados obtidos
    pass