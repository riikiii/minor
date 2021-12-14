from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Tags(models.Model):

    CATEGORY = (
        ('blood donor', 'blood donor'),
        ('organ donor', 'organ donor'),
        ('organ recipient', 'organ recipient'),
        ('volunteer', 'volunteer')
    ) 

    name = models.CharField(max_length=100, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name


class Donor(models.Model):

    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    social_handle = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    city= models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=200, null=True)
    age = models.IntegerField(default=18, null=True)
    type = models.ManyToManyField(Tags)
    date_created = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class Post(models.Model):

    donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    story = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.title[:40]
