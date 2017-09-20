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


def format_exam_date(exam_date_model):
    if not exam_date_model:
        return None

    exam_date = exam_date_model.exam_date
    if exam_date:
        return exam_date.strftime('%B {d}, %Y').format(d=exam_date.day)
    return None
