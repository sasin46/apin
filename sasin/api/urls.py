from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<int:pk>/', MovieDetailView.as_view()),
    path('halls/', HallListCreateView.as_view()),
    path('halls/<int:pk>/', HallDetailView.as_view()),
    path('clients/', ClientListCreateView.as_view()),
    path('clients/<int:pk>/', ClientDetailView.as_view()),
    path('sessions/', SessionListCreateView.as_view()),
    path('sessions/<int:pk>/', SessionDetailView.as_view()),
]