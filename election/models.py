from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=False)


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=20)
    votes = models.IntegerField()


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=7)
    has_voted = models.BooleanField(default=False)
