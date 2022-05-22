from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "search/<int:pk>/",
        views.mood_search,
        name="search",
    ),
    path(
        "result/<int:pk>/",
        views.mood_result,
        name="result",
    ),
    path(
        "test/",
        views.test,
        name="test",
    ),
]