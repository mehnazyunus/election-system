from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView
from .models import User, Candidate, Voter
from .forms import CandidateSignUpForm, VoterSignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
        return redirect('signup')


class VoterSignUpView(CreateView):
    model = User
    form_class = VoterSignUpForm
    template_name = 'voter_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'voter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('signup')


@method_decorator([login_required], name='dispatch')
class CandidateDetailsView(generic.DetailView):
    model = Candidate
    template_name = 'candidate_details.html'


@method_decorator([login_required], name='dispatch')
class VoterDetailsView(generic.DetailView):
    model = Voter
    template_name = 'voter_details.html'


def candidate_profiles(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_profiles.html', {'candidates': candidates})


def login_candidate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                # return render(request, 'candidate_details.html')  # , {'albums': albums})
                return redirect('candidate_details', pk=user.candidate.pk)
            else:
                return render(request, 'candidate_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'candidate_login.html', {'error_message': 'Invalid login'})
    return render(request, 'candidate_login.html')


def login_voter(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                # return render(request, 'base.html')  # , {'albums': albums})
                return redirect('voter_details', pk=user.voter.pk)
            else:
                return render(request, 'voter_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'voter_login.html', {'error_message': 'Invalid login'})
    return render(request, 'voter_login.html')


def logout(request):
    logout(request)
    return render(request, 'signup.html', context=None)
