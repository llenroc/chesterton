import React from 'react'
import {
  Route,
  Link
} from 'react-router-dom'
import Home from '../home'
import About from '../about'
import Account from '../account'
import OptionOrders from '../option_orders'
import OptionPositions from '../option_positions'
import {
  Container,
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';


class AppHeader extends React.Component {
    constructor(props) {
      super(props);

      this.toggle = this.toggle.bind(this);
      this.state = {
        isOpen: false
      };
    }
    toggle() {
      this.setState({
        isOpen: !this.state.isOpen
      });
    }
    render() {
      return (
        <div>
          <Navbar color="light" light expand="md">
            <Container>
              <NavbarBrand tag={Link} to="/">Chesterton</NavbarBrand>
              <NavbarToggler onClick={this.toggle} />
              <Collapse isOpen={this.state.isOpen} navbar>
                <Nav className="mr-auto" navbar>
                  <NavItem>
                    <NavLink tag={Link} to="/home">Home</NavLink>
                  </NavItem>
                  <NavItem>
                    <NavLink tag={Link} to="/account">Account</NavLink>
                  </NavItem>
                  <NavItem>
                    <NavLink tag={Link} to="/option_orders">Option Orders</NavLink>
                  </NavItem>
                  <NavItem>
                    <NavLink tag={Link} to="/option_positions">Option Positions</NavLink>
                  </NavItem>
                </Nav>
              </Collapse>
            </Container>
          </Navbar>
        </div>
      );
    }
  }

const App = () => (
  <div>
    <AppHeader/>

    <Container>
      <main>
        <Route exact path="/" component={Home} />
        <Route exact path="/about-us" component={About} />
        <Route exact path="/account" component={Account} />
        <Route exact path="/option_orders" component={OptionOrders} />
        <Route exact path="/option_positions" component={OptionPositions} />
      </main>
    </Container>
  </div>
)

export default App
