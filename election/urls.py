from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('election/', include('election.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/candidate/', views.candidateSignUpView.as_view(), name='candidate_signup'),
    # path('accounts/signup/voter/', views.voterSignUpView.as_view(), name='voter_signup'),

]
