import React from 'react'
import { Route, Link } from 'react-router-dom'
import Home from '../home'
import About from '../about'
import Account from '../account'
import OptionOrders from '../option_orders'
import OptionPositions from '../option_positions'


const App = () => (
  <div>
    <header>
      <Link to="/">Home</Link> |
      <Link to="/account">Account</Link> |
      <Link to="/about-us">About</Link> |
      <Link to="/option_orders">OptionOrders</Link> |
      <Link to="/option_positions">OptionPositions</Link>
    </header>

    <main>
      <Route exact path="/" component={Home} />
      <Route exact path="/about-us" component={About} />
      <Route exact path="/account" component={Account} />
      <Route exact path="/option_orders" component={OptionOrders} />
      <Route exact path="/option_positions" component={OptionPositions} />
    </main>
  </div>
)

export default App
