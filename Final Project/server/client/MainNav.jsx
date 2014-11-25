/** @jsx React.DOM */
var React = require('react');

var Nav = require('react-bootstrap').Nav;
var Navbar = require('react-bootstrap').Navbar;
var NavItem = require('react-bootstrap').NavItem;

var routes = require('./routes');

var MainNav = React.createClass({
    propTypes: {
        current: React.PropTypes.number.isRequired
    },
    render: function() {
        return (
            <Navbar>
                <Nav activeKey={this.props.current}>
                    <NavItem key={1} href={"#" + routes.MAP}>Map</NavItem>
                    <NavItem key={2} href={"#" + routes.VIEWER}>Viewer</NavItem>
                    <NavItem key={3} href={"#" + routes.DELETE}>Delete</NavItem>
                </Nav>
            </Navbar>
        );
    }
});

module.exports = MainNav;
