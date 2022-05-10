from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("mood/", include("apps.decider.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("intro/", TemplateView.as_view(template_name="intro.html"), name="intro"),
    path("manual/", TemplateView.as_view(template_name="manual.html"), name="manual"),
]
