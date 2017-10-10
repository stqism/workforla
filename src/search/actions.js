var createQueryUpdate = function(query) {
  return {
    type: 'query-update',
    query: query
  }
}

var createResultUpdate = function(response) {
  return {
    type: 'result-update',
    results: response.data.results
  }
}

export { createQueryUpdate, createResultUpdate }
