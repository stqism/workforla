var initialState = {
  query: '',
  results: []
}

var jobSearchReducer = function(state, action) {
  if (typeof state === 'undefined') {
    return initialState
  }

  switch (action.type) {
    case 'query-update':
      return Object.assign({}, state, {
        query: action.query
      })
    case 'result-update':
      return Object.assign({}, state, {
        results: action.results
      })
    default:
      return state
  }

  return state
}

export { jobSearchReducer }
