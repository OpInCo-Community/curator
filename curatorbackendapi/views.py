from django.views.generic.base import TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import messages

class HomePageView(TemplateView):

    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["notices"] = Notice.objects.all()[:5]
    #     context["events"] = Event.objects.all()[:5]
    #     return context

class SubjectPageView(TemplateView):
    
    template_name = "pages/subjects.html"

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["notices"] = Notice.objects.all()[:5]
    #     context["events"] = Event.objects.all()[:5]
    #     return context
def signUp(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request,user)
            messages.success(request, f"User created and logged in successfully" )
            return redirect("/")
        
        else:
            return render(request, "sign-up.html", {"form": form})
    
    form = CustomUserCreationForm()
    
    return render(request, "sign-up.html", {"form": form})
