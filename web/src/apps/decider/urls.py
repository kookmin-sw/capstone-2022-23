from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "search/",
        views.mood_search,
        name="search",
    ),
    path(
        "result/",
        views.mood_result,
        name="result",
    ),
]
