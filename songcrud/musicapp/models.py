from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField() 

    def __str__(self):
        return self.first_name +' '+ self.last_name 


class Song(models.Model):
    title = models.CharField(max_length=10)
    date_released = models.CharField(max_length=10)
    likes = models.CharField(max_length=10)
    artiste_id = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title             


class Lyric(models.Model):
    content = models.TextField(max_length=200)
    song_id = models.IntegerField()
    Song = models.ForeignKey(Song, on_delete=models.CASCADE,)

    def __str__(self):
        return self.content

      
