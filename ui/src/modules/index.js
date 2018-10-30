import { combineReducers } from 'redux'
import counter from './counter'
import option_order_api from './option_order_api'
import option_position_api from './option_position_api'

export default combineReducers({
  counter,
  option_order_api,
  option_position_api
})
