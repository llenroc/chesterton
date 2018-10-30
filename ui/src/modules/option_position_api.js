export const FETCH_REQUESTED = 'option_position_api/FETCH_REQUESTED'
export const FETCH_PARSE = 'option_position_api/FETCH_PARSE'

const initialState = {
  isFetching: false,
  option_positions: []
}

export default (state = initialState, action) => {
  switch (action.type) {
    case FETCH_REQUESTED:
      return {
        ...state,
        isFetching: true
      }

    case FETCH_PARSE:
      return {
        ...state,
        isFetching: false,
        option_positions: action.option_positions
      }

    default:
      return state
  }
}

export const fetchAsync = () => {
  return dispatch => {
    dispatch({
      type: FETCH_REQUESTED
    })

    let url = "http://localhost:8888/api/v1/option_positions/fetch"

    return fetch(url)
      .then(
        res => res.json(),
        error => console.log("An error occured ", error)
      )
      .then(data => {
        dispatch({
          type: FETCH_PARSE,
          option_positions: data
        })
      })
  }
}
