from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

RATING = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=25)
    size = models.IntegerField()
    colorway = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    release_date = models.DateField('Release Date')
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
class Review(models.Model):
    review = models.TextField(max_length=200)
    date = models.DateField(default=timezone.now())
    rating = models.IntegerField(choices=RATING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.rating} - {self.review}"
    
    class Meta:
        ordering = ['-date']

class Bid(models.Model):
    date = models.DateField(default=timezone.now())
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Placed bid of {self.amount} on {self.date}"
    
    class Meta:
        ordering = ['-amount']







