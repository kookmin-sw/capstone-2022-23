from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import tasks
from .models import Site, Result
from django.conf import settings

@login_required
def mood_search(request):
    # bar = tasks.crawl()
    # taewon = tasks.get_crawling_text_return_mood()
    # context = {"taewon": taewon}
    # return render(request, "search.html", context)
    return render(request, "search.html")


@login_required
def mood_result(request, pk):
    if request.method == 'POST':
        url = request.POST['input_url']
        user = request.user
        site = Site(url=url)
        site.save()
        Result.objects.create(url=site, user=user)
        result = Result.objects.all()
        only_text = tasks.get_crawling_text_return_mood(url)
        # context = {"target": tast_result}
        
        
    
    user_result_list = Result.objects.filter(user=request.user)
    return render(
        request,
        "result.html", {'result_list':user_result_list, "only_text":only_text}
    )
