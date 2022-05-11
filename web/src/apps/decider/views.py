from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def mood_search(request):
    return render(
        request,
        "search.html",
    )


@login_required
def mood_result(request):
    return render(
        request,
        "result.html",
    )
