from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/candidate/', views.CandidateSignUpView.as_view(), name='candidate_signup'),
    path('accounts/signup/voter/', views.VoterSignUpView.as_view(), name='voter_signup'),
    path('accounts/login/voter_login/', views.login_voter, name='voter_login'),
    path('accounts/login/candidate_login/', views.login_candidate, name='candidate_login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('candidate/<int:pk>', views.CandidateDetailsView.as_view(), name='candidate_details'),
    path('voter/<int:pk>', views.VoterDetailsView.as_view(), name='voter_details'),
    path('candidate_profiles', views.candidate_profiles, name='candidate_profiles'),
    path('voter/vote_preview', views.vote_preview, name='vote_preview')
]
