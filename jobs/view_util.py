from collections import namedtuple

from common import util


JobDetails = namedtuple(
    'JobDetails',
    ['title',
     'salary_low',
     'salary_high',
     'description',
     'responsibilities',
     'qualifications',
     'exam_notes'])


def make_job_details(job_class):
    return JobDetails(
        title=job_class.title,
        description=job_class.description,
        salary_low=util.format_currency(job_class.salary_low),
        salary_high=util.format_currency(job_class.salary_high),
        responsibilities=job_class.responsibilities,
        qualifications=job_class.qualifications,
        exam_notes=job_class.exam_notes)
