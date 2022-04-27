from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="mooddecider/index.html"), name="index"
    ),
    path(
        "whymd/",
        TemplateView.as_view(template_name="mooddecider/whymd.html"),
        name="whymd",
    ),
    path(
        "manual/",
        TemplateView.as_view(template_name="mooddecider/manual.html"),
        name="manual",
    ),
    path(
        "search/",
        views.mood_search,
        name="search",
    ),
    path(
        "result/",
        views.mood_search_result,
        name="result",
    ),
]
