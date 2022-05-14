from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import tasks


@login_required
def mood_search(request):
    bar = tasks.crawl()
    context = {"foo": bar}
    return render(request, "search.html", context)


@login_required
def mood_result(request):
    return render(
        request,
        "result.html",
    )
