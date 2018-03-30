from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, Voter, User
from django.db import transaction
from django.core.files.images import get_image_dimensions


class CandidateSignUpForm(UserCreationForm, forms.ModelForm):

    POST_CHOICES = [('President', 'President'),
                    ('General Secretary', 'General Secretary'),
                    ('Net Councillor', 'Net Councillor'), ]
    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)
    avatar = forms.ImageField()
    post = forms.CharField(label='Select the Post', widget=forms.Select(choices=POST_CHOICES))

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
        candidate.avatar = self.cleaned_data.get('avatar')
        candidate.post = self.cleaned_data.get('post')

        try:
            w, h = get_image_dimensions(candidate.avatar)

            # validate dimensions
            max_width = max_height = 2000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = candidate.avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(candidate.avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
           
            """Handles case when we are updating the user profile
            and do not supply a new avatar"""
            
            pass
        candidate.save()
        return user


class VoterSignUpForm(UserCreationForm):

    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)
    avatar = forms.ImageField()
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
        voter.avatar = self.cleaned_data.get('avatar')

        try:
            w, h = get_image_dimensions(voter.avatar)

            # validate dimensions
            max_width = max_height = 2000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = voter.avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(voter.avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:

            """Handles case when we are updating the user profile
            and do not supply a new avatar"""

            pass

        voter.save()
        return user
