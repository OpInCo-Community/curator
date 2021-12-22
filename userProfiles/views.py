from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.base import View
class UserProfile(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            user: user
        }
        return render(request, "userProfiles/profile.html", context)


