import React from 'react'


var Results = function(props) {
  var results = props.results.map(function(r) {
    return (<li key={r.id}>{r.title}</li>)
  })
  return (
    <div>
      {results}
    </div>
  )
}

var SearchForm = function(props) {
  return (
    <div>
      <form onSubmit={props.onSubmit}>
        <input type="text"
               placeholder="Search opportunities"
               value={props.query}
               onChange={props.onChange} />
      </form>
      <Results results={props.results} />
    </div>
  )
}

export { SearchForm }
