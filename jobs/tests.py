import datetime

from django.test import Client
from django.test import TestCase

from jobs.models import ExamDate
from jobs.models import JobClass


def _default_job_class_fields():
    return {
        'alias': 'accountant',
        'class_code': 1234,
        'classspec_id': 123456,
        'title': 'Accountant',
        'occupational_category': 'accounting 1.0.2',
        'skills': 'a,b,c',
        'related_keywords': 'd,e,f',
        'salary_low': 50000,
        'salary_high': 100000,
        'external_url': 'http://governmentjobs.com/accountant',
        'career_ladder_url': 'http://governmentjobs.com/accountant/career_ladder',
        'description': 'An accountant is a practitioner of accounting or accountancy.',
        'qualifications': 'Math.',
        'responsibilities': 'Doing math.',
        'exam_notes': 'Difficult.'
    }


class JobDetailsBaseCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.job = JobClass.objects.create(
            **_default_job_class_fields())
        self.job.save()

    def tearDown(self):
        self.job.delete()


class JobDetailsTestCase(JobDetailsBaseCase):

    def test_job_details_loads(self):
        response = self.client.get('/jobs/accountant')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['job'].title, 'Accountant')

    def test_no_exam_date(self):
        response = self.client.get('/jobs/accountant')
        self.assertContains(response, 'exam has not been scheduled')

    def test_404_for_bad_alias(self):
        response = self.client.get('/jobs/personal-assistant-for-leonard')
        self.assertEqual(response.status_code, 404)


class ExamDateTestCase(JobDetailsBaseCase):

    def setUp(self):
        super().setUp()
        self.exam_date = ExamDate.objects.create(
            class_code=1234,
            open_date=datetime.date(2020, 12, 1),
            exam_date=datetime.date(2020, 12, 31)
        )
        self.exam_date.save()

    def test_exam_date_shown(self):
        response = self.client.get('/jobs/accountant')
        self.assertContains(response, 'December 31, 2020')

    def tearDown(self):
        self.exam_date.delete()
        super().tearDown()
