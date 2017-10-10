import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import initSubscriber from 'redux-subscriber'

import { createResultUpdate } from './actions'
import { SearchFormContainer } from './containers'
import { jobSearchReducer } from './reducers'

var store = createStore(jobSearchReducer)
var subscribe = initSubscriber(store)

subscribe('query', function(state) {
  axios.get('/jobs/search?q=' + state.query)
    .then(function(resp) {
      store.dispatch(createResultUpdate(resp));
    })
})


ReactDOM.render(
  <Provider store={store}>
    <SearchFormContainer />
  </Provider>,
  document.getElementById('search-container')
)
