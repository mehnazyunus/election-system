from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/candidate/', views.CandidateSignUpView.as_view(), name='candidate_signup'),
    path('accounts/signup/voter/', views.VoterSignUpView.as_view(), name='voter_signup'),
    path('accounts/login/candidate', views.login_user, name='candidate_login'),
]
