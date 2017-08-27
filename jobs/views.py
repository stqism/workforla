import datetime
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from workforla.search.search_client import W4LASearch


def index(request):
    context = {'time': datetime.datetime.now().isoformat()}
    return render(request, 'jobs/index.html', context)

def search(request):
    query = request.GET['q']
    client = W4LASearch(settings.ES_SETTINGS)
    return JsonResponse(client.keyword_search(query))
