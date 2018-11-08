import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {
  fetchAsync
} from '../../modules/option_position_api'
import _ from 'lodash'

const sortByExpirationDate = (ops, field='expiration_date') => {
  return _.orderBy(ops, field, 'asc');
}

const OptionPositionsTable = (ops) => {
  const rows = ops.map((op) =>
    <tr key={op.id}>
      <td>{op.chain_symbol}</td>
      <td>{op.expiration_date}</td>
      <td>{op.strike_price}</td>
      <td>{op.quantity}</td>
      <td>{op.type}</td>
      <td>{op.option_type}</td>
      <td>{op.delta}</td>
      <td>{op.theta}</td>
      <td>{op.gamma}</td>
      <td>{op.vega}</td>
    </tr>
  )

  return (
    <table>
      <tbody>
        <tr>
          <th>Symbol</th>
          <th>Expiration Date</th>
          <th>Strike Price</th>
          <th>Quantity</th>
          <th>Type</th>
          <th>Option Type</th>
          <th>Delta</th>
          <th>Theta</th>
          <th>Gamma</th>
          <th>Vega</th>
        </tr>
        { rows }
      </tbody>
    </table>
  )
}

const OptionPositions = props => (
  <div>
    <h1>Option Positions</h1>
    <p>Count: {props.option_positions.length}</p>

    <p>
      <button onClick={props.fetchAsync} disabled={props.isFetching}>
        fetch Async
      </button>
    </p>

    { OptionPositionsTable(sortByExpirationDate(props.option_positions)) }
  </div>
)

const mapStateToProps = ({ option_position_api }) => ({
  isFetching: option_position_api.isFetching,
  option_positions: option_position_api.option_positions
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
)(OptionPositions)
