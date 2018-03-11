from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, Voter, User
from django.db import transaction

class CandidateSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ['user.username', 'user.password', 'post']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        if commit:
            user.save()
        return user


class VoterSignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_candidate = True
        user.save()
        voter = Voter.objects.create(user=user)
        voter.roll.add(*self.cleaned_data.get('name'))
        voter.roll.add(*self.cleaned_data.get('roll'))
        return user