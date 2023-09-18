from django.forms import ModelForm
from .models import Review, Bid

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

