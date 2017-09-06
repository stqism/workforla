from collections import namedtuple

from django.conf import settings

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


JOBS_INDEX = 'jobs'
SNIPPET_LENGTH = 200
QUERY_FIELDS = [
    'title',
    'description',
    'related_keywords',
    'categories'
]


class Hit(namedtuple(
    'Hit',
    'id alias title description categories')):
    """Simple container for results."""

    def to_json(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'title': self.title,
            'description': self.description,
            'categories': self.categories
        }


def search_by_keyword(query_string):
    """Generic search given a text query."""
    if not query_string:
        return []

    client = Elasticsearch([settings.ES_HOST])
    search = Search(using=client, index=JOBS_INDEX)
    search = search.query(
        'multi_match',
        query=query_string,
        fields=QUERY_FIELDS)
    response = search.execute()
    return [
        Hit(id=h.meta['id'],
            alias=h.alias,
            title=h.title,
            description=h.description[:SNIPPET_LENGTH],
            categories=list(h.categories))
        for h in response.hits
    ]
