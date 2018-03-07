from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, Voter, User


class CandidateSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        if commit:
            user.save()
        return user
