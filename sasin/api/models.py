from django.db import models

class Movie(models.Model):
    FilmId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    year = models.IntegerField()
    ticketprice = models.DecimalField(max_digits=10, decimal_places=2)

class Hall(models.Model):
    HallId = models.AutoField(primary_key=True)
    HallNumber = models.IntegerField()
    HallCleaning = models.CharField(max_length=100)

class Client(models.Model):
    ClientId = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    EmailAddress = models.EmailField(max_length=100)
    
class Session(models.Model):
    SessionId = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    StartDateTime = models.DateTimeField()
    TicketPrice = models.DecimalField(max_digits=10, decimal_places=2)
    EndDateTime = models.DateTimeField()