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
        "search/None/",
        views.mood_search,
        name="search_id_none",
    ),
    path(
        "result/None/",
        views.mood_search,
        name="result_id_none",
    ),
    path(
        "result/<int:pk>/",
        views.mood_result,
        name="result",
    ),
]
