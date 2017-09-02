import datetime
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from jobs.models import JobClass
from jobs.view_util import make_job_details
from workforla.search.search_client import W4LASearch


def index(request):
    context = {'time': datetime.datetime.now().isoformat()}
    return render(request, 'jobs/index.html', context)


def details(request, job_alias):
    job_class = JobClass.objects.get(alias=job_alias)
    context = {'job': make_job_details(job_class)}
    return render(request, 'jobs/details.html', context)


def search(request):
    query = request.GET['q']
    client = W4LASearch(settings.ES_SETTINGS)
    return JsonResponse(client.keyword_search(query))
