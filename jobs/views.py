import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from jobs.models import JobClass
from jobs.search_util import search_by_keyword
from jobs.view_util import make_job_details


def index(request):
    context = {'time': datetime.datetime.now().isoformat()}
    return render(request, 'jobs/index.html', context)


def details(request, job_alias):
    job_class = get_object_or_404(JobClass, alias=job_alias)
    context = {'job': make_job_details(job_class)}
    return render(request, 'jobs/details.html', context)


def search(request):
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse({'count': 0, 'results': []})

    hits = search_by_keyword(query)
    return JsonResponse({
        'count': len(hits),
        'results': [h.to_json() for h in hits]
    })
