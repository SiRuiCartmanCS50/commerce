from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Listing(models.Model):
    seller = models.CharField(max_length=1000) 
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    starting_bid = models.IntegerField()
    category = models.CharField(max_length=20)
    image_link = models.CharField(max_length=5000000, default=None, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    newbid = models.IntegerField(default=0, blank=False, null=True)
    newbiduser = models.CharField(max_length=1000, default=None, blank=True, null=True)
    listing = models.IntegerField(default=True, blank=True, null=True)


class Comment(models.Model):
    user = models.CharField(max_length=500, blank=True, null=True)
    comment = models.CharField(max_length=500)
    listingid = models.IntegerField()
    commented_time = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    userr = models.CharField(max_length=500, null=True, blank=True) 
    bid = models.IntegerField(null=True, blank=True)
    listing = models.CharField( max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    
class ActiveWatchlist(models.Model):
    user = models.CharField(max_length=64, blank=True, null=True)
    listingid = models.IntegerField(null=True, blank=True)