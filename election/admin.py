from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Candidate, Voter, Election

admin.site.register(User, UserAdmin)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Election)


# Register your models here.
# admin
# admin@example.com
# pass1234
