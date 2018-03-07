# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView
from .models import User, Candidate, Voter
from .forms import CandidateSignUpForm

# Create your views here.


class SignUpView(TemplateView):
    template_name = 'signup.html'


class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'candidate_signup.html'



