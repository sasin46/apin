from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, Hall, Client, Session
from django.http import HttpResponse

class MovieListView(ListView):
    model = Movie
   
class HallListView(ListView):
    model = Hall
   
class ClientListView(ListView):
    model = Client

class SessionListView(ListView):
    model = Session
    queryset = Session.objects.all()
   
def get_queryset(self):
       
        return self.queryset.filter(...)