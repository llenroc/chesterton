import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {
  fetchAsync
} from '../../modules/option_order_api'
import { Button } from 'reactstrap';
import { Table } from 'reactstrap';


const OptionOrdersTable = (oos) => {
  console.log(oos)
  const rows = oos.map((oo) =>
    <tr key={oo.id}>
      <td>{oo.id}</td>
      <td>{oo.chain_symbol}</td>
      <td>{oo.expiration_date}</td>
      <td>{oo.strike_price}</td>
    </tr>
  )

  return (
    <Table striped hover>
      <tbody>
        <tr>
          <th>Id</th>
          <th>Symbol</th>
          <th>Expiration Date</th>
          <th>Strike Price</th>
        </tr>
        { rows }
      </tbody>
    </Table>
  )
}

const OptionOrders = props => (
  <div>
    <h1>Option Orders</h1>
    <p>Count: {props.option_orders.length}</p>

    <p>
      <button onClick={props.fetchAsync} disabled={props.isFetching}>
        fetch Async
      </button>
    </p>

    { OptionOrdersTable(props.option_orders) }
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
