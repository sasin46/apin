from django.db import models

class Movie(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    year = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

class Hall(models.Model):
    hall_id = models.AutoField(primary_key=True)
    hall_number = models.IntegerField()
    hall_cleaning = models.CharField(max_length=100)

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_datetime = models.DateTimeField()
