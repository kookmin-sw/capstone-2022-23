from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def mood_search(request):
    return render(
        request,
        "mooddecider/search.html",
    )


@login_required
def mood_search_result(request):
    return render(
        request,
        "mooddecider/result.html",
    )
