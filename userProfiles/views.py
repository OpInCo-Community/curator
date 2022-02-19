from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse

from django.views.generic.base import View
from .forms import CustomUserUpdateForm
class UserProfile(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        user_form = CustomUserUpdateForm(instance=user)
        curations_count=user.curations.all().count() 
        print(user_form)
        context = {
            "user": user,
            "user_form": user_form,
            "curations_count":curations_count
        }
        return render(request, "userProfiles/profile.html", context)

    def post(self, request, *args, **kwargs):
        
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)

        if user_form.is_valid(): 
            user_form.save()
            # messages.add_message(request, messages.SUCCESS, "Your profile has been updated")
            return redirect(reverse("profile"))

        return render(request, "customer/profile.html",
            { "user_form": user_form,
                })
