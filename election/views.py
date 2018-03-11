from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView
from .models import User, Candidate, Voter
from .forms import CandidateSignUpForm, voterSignUpForm
from django.contrib.auth import login

# Create your views here.


class SignUpView(TemplateView):
    template_name = 'signup.html'


class CandidateSignUpView(CreateView):
    model = User
    form_class = CandidateSignUpForm
    template_name = 'candidate_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'candidate'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts/signup')


class voterSignUpView(CreateView):
    model = User
    form_class = voterSignUpForm
    template_name='voter_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'voter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts/signup')