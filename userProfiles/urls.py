from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path("profile/", views.UserProfile.as_view(), name="profile"),
]
