import datetime
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from jobs.models import JobClass
from jobs.view_util import make_job_details


def index(request):
    context = {'time': datetime.datetime.now().isoformat()}
    return render(request, 'jobs/index.html', context)


def details(request, job_alias):
    job_class = get_object_or_404(JobClass, alias=job_alias)
    context = {'job': make_job_details(job_class)}
    return render(request, 'jobs/details.html', context)
