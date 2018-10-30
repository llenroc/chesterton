import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {
  fetchAsync
} from '../../modules/option_position_api'

const OptionPositionsTable = (ops) => {
  const rows = ops.map((op) =>
    <tr key={op.id}>
      <td>{op.id}</td>
      <td>{op.chain_symbol}</td>
      <td>{op.quantity}</td>
      <td>{op.type}</td>
    </tr>
  )

  console.log(ops)

  return (
    <table>
      <tbody>
        <tr>
          <th>ID</th>
          <th>Symbol</th>
          <th>Quantity</th>
          <th>Type</th>
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

    { OptionPositionsTable(props.option_positions) }
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
