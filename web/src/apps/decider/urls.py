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
        "result/<int:pk>/delete/",
        views.delete_result,
        name="delete",
    ),
    path(
        "result/<int:pk>/",
        views.mood_result,
        name="result",
    ),
  
    
]