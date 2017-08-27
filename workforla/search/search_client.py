# -*- coding: utf-8 -*-
import elasticsearch


KEYWORD_SEARCH_FIELDS = ['title', 'skills', 'related_keywords']


# TODO:
# + error checking / handling
# + retry logic?
class W4LASearch:
    """Client for running queries against ElasticSearch.

    Arguments:
    settings -- Python dictionary containing 'host', 'username',
        'password', and 'port' keys.
    """

    INDEX = 'w4la'
    DOC_TYPE = 'job'

    def __init__(self, settings):
        self._client = elasticsearch.Elasticsearch(
            [settings['host']],
            http_auth=(settings['username'], settings['password']),
            port=settings['port'])

    def get_job_by_id(self, _id):
        result = self.search({'query': {'match': {'_id': _id}}})
        [hit] = result['hits']['hits']
        return hit['_source']

    def keyword_search(self, search_query):
        result = self.search({
            'query': {
                'query_string': {
                    'fields': KEYWORD_SEARCH_FIELDS,
                    'query': search_query
                }
            }
        })
        return result['hits']

    def search(self, query_body):
        """Issue a search using the provided query body in Query DSL format."""
        return self._client.search(
            index=self.INDEX,
            doc_type=self.DOC_TYPE,
            body=query_body)
