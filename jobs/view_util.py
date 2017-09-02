from collections import namedtuple

from common import util


JobDetails = namedtuple(
    'JobDetails',
    ['title',
     'salary_low',
     'salary_high',
     'description'])


def make_job_details(job_class):
    return JobDetails(
        title=job_class.title,
        description=job_class.description,
        salary_low=util.format_currency(job_class.salary_low),
        salary_high=util.format_currency(job_class.salary_high))
