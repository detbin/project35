from django.db import models
from django.urls import reverse
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_lenght=128, help_text='Introduce el nombre de la pelicula:')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    resume = models.TextField(maxlenght=180, help_text='Introduce el argumento de la pelicula:')
    genre = models.ManyToManyField(Genre)
    dateofmovie = models.DateField('Año de la pelicula', null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ISDN de la pelicula')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_details', args=[str(self.id)])


class Director(models.Model):
    firstname = models.CharField(max_lenght=128, help_text='Introduce el nombre del director:')
    lastname = models.CharField(max_lenght=128, help_text='Introduce el apellido del director:')

    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)
