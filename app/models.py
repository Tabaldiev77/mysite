from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=80)
    year = models.IntegerField()
    director = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    operator = models.CharField(max_length=70)
    rating_value = models.FloatField()
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=77)
    age = models.IntegerField(default=0)
    time = models.TimeField()
    producer = models.CharField(max_length=70)
    operator = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title







