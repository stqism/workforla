import { connect } from 'react-redux'

import { SearchForm } from './components'
import { createQueryUpdate } from './actions'


var mapStateToProps = function(state) {
  return {
    query: state.query,
    results: state.results
  }
}

var mapDispatchToProps = function(dispatch) {
  return {
    onSubmit: function(evt) {
      evt.preventDefault()
    },
    onChange: function(evt) {
      dispatch(createQueryUpdate(evt.target.value))
    }
  }
}

var SearchFormContainer = connect(mapStateToProps, mapDispatchToProps)(SearchForm)

export { SearchFormContainer }
