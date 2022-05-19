from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import tasks
from .models import Site, Result
from django.conf import settings


@login_required
def mood_search(request, pk):
    if request.method == "POST":
        url = request.POST["input_url"]
        user = request.user

        site = Site(url=url)
        site.save()

        Result.objects.create(url=site, user=user)
        tasks.trigger(user, site)
    return render(request, "search.html")


@login_required
def mood_result(request, pk):
    user = request.user

    if request.method == "POST":
        url = request.POST["input_url"]

        site = Site(url=url)
        site.save()

        Result.objects.create(url=site, user=user)
        tasks.trigger(user, site)

        user_result_list = Result.objects.filter(user=user)
        return render(request, "result.html", {"result_list": user_result_list})
    elif request.method == "GET":
        user_result_list = Result.objects.filter(user=user)
        return render(request, "result.html", {"result_list": user_result_list})
    else:
        return render(request, "intro.html")


def test(request):
    if request.method == "POST":
        url = request.POST["input_url"]
        user = request.user

        site = Site(url=url)
        site.save()

        Result.objects.create(url=site, user=user)
        tasks.trigger(user, site)

        return render(request, "test.html")
