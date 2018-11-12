export const FETCH_REQUESTED = 'option_order_api/FETCH_REQUESTED'
export const FETCH_PARSE = 'option_order_api/FETCH_PARSE'
// export const INDEX_REQUESTED = 'option_order_api/INDEX_REQUESTED'
// export const INDEX_PARSE = 'option_order_api/INDEX_PARSE'

const initialState = {
  isFetching: false,
  option_orders: []
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
        option_orders: action.option_orders
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

    let url = "http://localhost:8888/api/v1/option_orders"

    return fetch(url)
      .then(
        response => response.json(),
        error => console.log("An error occured ", error)
      )
      .then(data => {
        dispatch({
          type: FETCH_PARSE,
          option_orders: data
        })
      })
  }
}

// export const indexAsync = () => {
//   return dispatch => {
//     dispatch({
//       type: INDEX_REQUESTED
//     })
//
//     let url = "http://localhost:8888/api/v1/option_orders"
//
//     return fetch(url)
//       .then(
//         res => res.json(),
//         error => console.log("An error occured ", error)
//       )
//       .then(json => {
//         dispatch({
//           type: INDEX_PARSE,
//           option_orders: json
//         })
//       })
//   }
// }
