from django.views.generic import View, ListView
from django.contrib.auth import login
from django.shortcuts import redirect, render

from curations.models import Curation, Subject
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


class HomePageView(View):
    template_name = "pages/home.html"

    def get(self, request):
        subjects = Subject.objects.all()
        curations_whole = Curation.objects.order_by("-upvotes")[:15]

        # pagination stuff
        p = Paginator(curations_whole, 15)
        page = request.GET.get("page")
        curations = p.get_page(page)

        # setting the context
        context = {}
        context["curations"] = curations
        context["subjects"] = subjects
        return render(request, self.template_name, context)


class SubjectListView(ListView):
    model = Subject
    context_object_name = ""
    template_name = "pages/subject_list.html"


class SubjectPageView(View):
    template_name = "pages/subjects.html"

    def get(self, request, *args, **kwargs):
        # defining vars
        title = kwargs["sub"]
        subject = Subject.objects.filter(title=title)[0]
        curation_count = subject.curations.all().count()
        # filtering Data
        search_term = request.GET.get("search")
        if search_term:
            curations_whole = Curation.objects.filter(
                Q(title__contains=search_term) | Q(description__contains=search_term),
                subject=subject,
            ).order_by("-upvotes")
        else:
            curations_whole = Curation.objects.filter(subject=subject).order_by(
                "-upvotes"
            )

        # pagination stuff
        p = Paginator(curations_whole, 15)
        page = request.GET.get("page")
        curations = p.get_page(page)

        # setting the context
        context = {}
        context["curations"] = curations
        context["subject"] = subject
        context["curation_count"] = curation_count

        return render(request, self.template_name, context)


def signUp(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request, user)
            messages.success(request, f"User created and logged in successfully")
            return redirect("/")

        else:
            return render(request, "sign-up.html", {"form": form})

    form = CustomUserCreationForm()

    return render(request, "sign-up.html", {"form": form})


def add_curation_view(request):
    return render(request, "pages/curation_add.html")
