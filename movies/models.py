from django.db import models

class Genre(models.Model):
    # genre_choices = [
    #     "Adventure",
    #     "Action",
    #     "Family",
    #     "Fantasy",
    #     "Musical",
    #     "Sci-Fi"
    # ]
    # Tried using choices but who am I kidding? 
    # I'd rather just let the user enter garbage genre than sort through this mess.
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# I'd use a Director class to probably showcase the director's movies in future iterations but 
# since we do not have time to go through every director to add them first before populating movies,
# I'm just going to provide CharField to director in Movie model for now.
# class Director(models.Model):
#     name = models.CharField(max_length = 50)



class Movie(models.Model):
    name = models.CharField(max_length=100)
    # director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    director = models.CharField(max_length=100)
    ninetyninepop = models.FloatField(default=0)
    imdb_rate = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name



