import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {
  fetchAsync
} from '../../modules/option_order_api'

const OptionOrders = props => (
  <div>
    <h1>Option Orders</h1>
    <p>Count: {props.option_orders.length}</p>

    <p>
      <button onClick={props.fetchAsync} disabled={props.isFetching}>
        fetch Async
      </button>
    </p>
  </div>
)

const mapStateToProps = ({ option_order_api }) => ({
  isFetching: option_order_api.isFetching,
  option_orders: option_order_api.option_orders
})

const mapDispatchToProps = dispatch =>
  bindActionCreators(
    {
      fetchAsync,
    },
    dispatch
  )

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(OptionOrders)
