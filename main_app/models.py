from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

SIZE = (
    (6.0, '6'),
    (6.5, '6.5'),
    (7.0, '7'),
    (7.5, '7.5'),
    (8.0, '8'),
    (8.5, '8.5'),
    (9.0, '9'),
    (9.5, '9.5'),
    (10.0, '10'),
    (10.5, '10.5'),
    (11.0, '11'),
    (11.5, '11.5'),
    (12.0, '12'),
    (12.5, '12.5'),
    (13.0, '13'),
    (13.5, '13.5'),
    (14.0, '14'),
    (14.5, '14.5'),
    (15.0, '15'),
    (15.5, '15.5'),
    (16.0, '16'),
)

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=25)
    size = models.DecimalField(max_digits=3, decimal_places=1, choices=SIZE)
    colorway = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    release_date = models.DateField('Release Date')
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} - Click here for details'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date']
    
class Review(models.Model):
    review = models.TextField(max_length=200)
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField(choices=RATING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.rating} - {self.review}"
    
    class Meta:
        ordering = ['-date']

class Bid(models.Model):
    date = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Placed bid of {self.amount} on {self.date}"
    
    class Meta:
        ordering = ['-amount']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for shoe_id: {self.shoe_id} @{self.url}"







