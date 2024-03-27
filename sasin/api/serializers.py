from rest_framework import serializers
from .models import Movie, Hall, Client, Session
from rest_framework import generics
from .serializers import MovieSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('film_id', 'title', 'director', 'genre', 'duration', 'year', 'ticket_price')

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('hall_id', 'hall_number', 'hall_cleaning')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'last_name', 'first_name', 'email_address')

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session

        fields = ('session_id', 'movie', 'hall', 'start_datetime', 'ticket_price', 'end_datetime')

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer