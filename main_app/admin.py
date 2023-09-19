from django.contrib import admin

from .models import Shoe, Review, Bid, Photo

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Review)
admin.site.register(Bid)
admin.site.register(Photo)