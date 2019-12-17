from django.db import models

# Create your models here.
class GithubRecord(models.Model):
    #Store the list of repositories in a database table. 
    #The table must contain the 
    #repository ID
    #, name
    #, URL
    #, created date
    #, last push date
    #, description
    #, and number of stars. 
    repository_ID = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    last_push_date = models.DateTimeField()
    description = models.CharField(max_length=200)
    stars = models.PositiveIntegerField()
    