from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView
from .models import User, Candidate, Voter, Election
from .forms import CandidateSignUpForm, VoterSignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Max

# Create your views here.


@method_decorator([login_required], name='dispatch')
class CandidateDetailsView(generic.DetailView):
    model = Candidate
    template_name = 'candidate_details.html'


def candidate_profiles(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_profiles.html', {'candidates': candidates})


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
        return redirect('candidate_details', pk=user.candidate.pk)


class SignUpView(TemplateView):
    template_name = 'signup.html'


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
        return redirect('voter_details', pk=user.voter.pk)


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


def vote(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    try:
        if not request.user.voter.has_voted:
            candidate.votes += 1
            request.user.voter.has_voted = True
            request.user.voter.save()
            candidate.save()

    except (KeyError, Candidate.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        messages.success(request, 'Vote successful!')
        return redirect('voter_details', pk=request.user.voter.pk)


def vote_confirm(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'vote_confirm.html', {'candidate': candidate})


@method_decorator([login_required], name='dispatch')
class VoterDetailsView(generic.DetailView):
    model = Voter
    template_name = 'voter_details.html'


def vote_preview(request):
    candidates = Candidate.objects.all()
    return render(request, 'vote_preview.html', {'candidates': candidates})


def results(request):
    election = get_object_or_404(Election, pk=1)
    max_votes = Candidate.objects.all().aggregate(Max('votes'))
    winners = Candidate.objects.all().filter(votes__exact=max_votes['votes__max'])
    return render(request, 'results.html', {'election': election, 'winners': winners})
