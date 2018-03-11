from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, Voter, User
from django.db import transaction


class CandidateSignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        user.save()
        candidate = Candidate.objects.create(user=user)
        candidate.name = self.cleaned_data.get('name')
        candidate.roll = self.cleaned_data.get('roll')
        candidate.save()
        return user


class VoterSignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_voter = True
        user.save()
        voter = Voter.objects.create(user=user)
        voter.name = self.cleaned_data.get('name')
        voter.roll = self.cleaned_data.get('roll')
        voter.save()
        return user
