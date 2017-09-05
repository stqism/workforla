from elasticsearch_dsl.connections import connections

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch

from django.conf import settings
from jobs.models import JobClass
from jobs.search_models import JobClassIndex


connections.create_connection(hosts=[settings.ES_HOST])


def format_job_for_indexing(job_model):
    record = JobClassIndex(
        meta={
            'id': job_model.id,
            'alias': job_model.alias
        },
        title=job_model.title,
        description=job_model.description,
        qualifications=job_model.qualifications,
        categories=[c.name for c in job_model.categories.all()],
        skills=job_model.skills,
        related_keywords=job_model.related_keywords,
        salary_low=job_model.salary_low,
        salary_high=job_model.salary_high)
    record.save()
    return record.to_dict(include_meta=True)


def create_jobs_index():
    es = Elasticsearch([settings.ES_HOST])
    es.indices.create(index='jobs')


def index_all_jobs():
    JobClassIndex.init(index='jobs')
    es = Elasticsearch([settings.ES_HOST])
    actions = [format_job_for_indexing(job)
               for job in JobClass.objects.all().iterator()]
    bulk(client=es, actions=actions)
