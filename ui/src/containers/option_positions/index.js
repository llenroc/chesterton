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

const SummaryTable = (ops) => {
  const things = _.uniqBy(ops, 'chain_symbol');
  const symbols = _.map(things, 'chain_symbol');

  const results = _.map(symbols, (symbol) => {
    let sops = _.filter(ops, (x) => x.chain_symbol === symbol)

    let delta = sops.reduce((a, e) => {return a + parseFloat(e.delta)}, 0).toFixed(4);
    let theta = sops.reduce((a, e) => {return a + parseFloat(e.theta)}, 0).toFixed(4);
    let gamma = sops.reduce((a, e) => {return a + parseFloat(e.gamma)}, 0).toFixed(4);
    let vega = sops.reduce((a, e) => {return a + parseFloat(e.vega)}, 0).toFixed(4);
    let quantity = sops.length

    return {
      cid: symbol,
      chain_symbol: symbol,
      quantity: quantity,
      delta: delta,
      theta: theta,
      vega: vega,
      gamma: gamma
    }
  })

  const rows = _.map(results, (r) =>
    <tr key={r.cid}>
      <td>{r.chain_symbol}</td>
      <td>{r.quantity}</td>
      <td>{r.delta}</td>
      <td>{r.theta}</td>
      <td>{r.gamma}</td>
      <td>{r.vega}</td>
    </tr>
  )

  return (
    <table key="summary_table">
      <tbody>
        <tr>
          <th>Symbol</th>
          <th>Quantity</th>
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
    <table key="detail_table">
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

    { SummaryTable(props.option_positions) }

    <br/>
    <br/>

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
