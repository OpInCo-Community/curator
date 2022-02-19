from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

admin.site.site_header = "CURATOR"
admin.site.site_title = "CURATOR ADMIN PORTAL"
admin.site.index_title = "Welcome to Curator admin portal"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("userProfiles.urls")),
    path(
        'sign-in/"',
        auth_views.LoginView.as_view(template_name="sign-in.html"),
        name="sign-in",
    ),
    path("sign-out/", auth_views.LogoutView.as_view(next_page="/"), name="sign-out"),
    path("sign-up/", views.signUp, name="sign-up"),
    path("subjects/", views.SubjectListView.as_view(), name="subjects"),
    path("subject/<str:sub>", views.SubjectPageView.as_view(), name="subject"),
    path("", views.HomePageView.as_view(), name="home"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
