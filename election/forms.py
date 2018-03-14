from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Candidate, Voter, User
from django.db import transaction
from django.core.files.images import get_image_dimensions


class CandidateSignUpForm(UserCreationForm, forms.ModelForm):

    name = forms.CharField(max_length=30)
    roll = forms.CharField(max_length=7)
    avatar = forms.ImageField()

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
        candidate.save()
        return user
        """try:
            w, h = get_image_dimensions(candidate.avatar)

            # validate dimensions
            max_width = max_height = 100
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
           
            Handles case when we are updating the user profile
            and do not supply a new avatar
            
            pass"""






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
