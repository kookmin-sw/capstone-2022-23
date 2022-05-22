from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import tasks
from .models import Site, Result
from django.conf import settings
import time, math, datetime


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

    if request.method == "GET":
        user_result_list = Result.objects.filter(user=user)
        # created_at =
        # context = {
        #     "result_list": user_result_list,
        # }
        converted_time_list = []
        for result in user_result_list:
            converted_time_list.append(result.created_at.timestamp() * 1000)

        converted_time_list = convert_time(converted_time_list)
        # for user_result, converted_time in zip(user_result_list, converted_time_list):
        #     user_result["converted_time"] = converted_time

        return render(
            request,
            "result.html",
            {"result_list": zip(user_result_list, converted_time_list)},
        )
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


def convert_time(result_time_list):
    # 1653245057: millis
    # 1653237597324.5151
    now_fd = []  # 계산된 시간 저장 리스트
    for result_time in result_time_list:
        millis = int(round(time.time()))
        me_time = (millis - (result_time / 1000)) / 60
        me_timehour = math.floor((me_time / 60))
        me_timeday = math.floor((me_timehour / 24))
        me_timeyear = math.floor(me_timeday / 365)

        if me_time < 1:
            now_fd.append("방금전")

        elif me_time < 60:
            a = str(me_time) + "분전"
            now_fd.append(a)

        elif me_timehour < 24:
            a = str(me_timehour) + "시간전"
            now_fd.append(a)

        elif me_timeday < 365:
            a = str(me_timeday) + "일전"
            now_fd.append(a)

        elif me_timeyear >= 1:
            a = str(me_timeyear) + "년전"
            now_fd.append(a)

    return now_fd
