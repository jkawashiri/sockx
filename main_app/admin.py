from django.contrib import admin

from .models import Shoe, Review

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Review)