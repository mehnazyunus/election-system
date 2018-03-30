from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_voter = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=20, default='post')
    votes = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default="votername")
    roll = models.CharField(max_length=7, default="rollno")
    avatar = models.ImageField(default="https://upload.wikimedia.org/wikipedia/commons/6/67/User_Avatar.png")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' : ' + self.user.username


class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="votername")
    roll = models.CharField(max_length=7, default="rollno")
    has_voted = models.BooleanField(default=False)
    has_voted_a = models.BooleanField(default=False)
    has_voted_b = models.BooleanField(default=False)
    has_voted_c = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    avatar = models.ImageField(default="https://upload.wikimedia.org/wikipedia/commons/6/67/User_Avatar.png")

    def __str__(self):
        return self.name + ':' + self.user.username


class Election(models.Model):
    started = models.BooleanField(default=False)
    ended = models.BooleanField(default=True)
