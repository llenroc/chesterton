import React from 'react'
import { Route, Link } from 'react-router-dom'
import Home from '../home'
import About from '../about'
import Account from '../account'

const App = () => (
  <div>
    <header>
      <Link to="/">Home</Link>
      <Link to="/account">Account</Link>
      <Link to="/about-us">About</Link>
    </header>

    <main>
      <Route exact path="/" component={Home} />
      <Route exact path="/about-us" component={About} />
      <Route exact path="/account" component={Account} />
    </main>
  </div>
)

export default App
