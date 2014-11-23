/** @jsx React.DOM */
var React = require('react');
var Backbone = require('backbone');
var $ = require('jquery');
Backbone.$ = $;

var Well = require('react-bootstrap').Well;

var MainNav = require('./MainNav');
var DataList = require('./DataList');
var routes = require('./routes');


var InterfaceComponent = React.createClass({
    componentWillMount : function() {
        this.callback = (function() {
            this.forceUpdate();
        }).bind(this);

        this.props.router.on("route", this.callback);
    },
    componentWillUnmount : function() {
        this.props.router.off("route", this.callback);
    },
    render: function() {
        var nav = 0;
        var content;
        if (this.props.router.current[0] == routes.MAP) {
            nav = 1;
            content = (
                <Well>
                    <p>Welcome! this will be a map one day</p>
                </Well>
            );
        }
        if (this.props.router.current[0] == routes.VIEWER) {
            nav = 2;
            content = (
                <Well>
                    <DataList />
                </Well>
            );
        }
        if (this.props.router.current[0] == routes.DELETE) {
            nav = 3;
            content = (
                <Well>
                    <p>We can delete data here if necessary?</p>
                </Well>
            );
        }
        return (
            <div className="content">
                <MainNav current={nav} />
                <Well>
                    {content}
                </Well>
            </div>
        );
    }
});

var Router = Backbone.Router.extend({
    current: ['home'],
    routes: {
        '*actions': function(actions) {
            if (actions) {
                this.current = actions.split('/');
            } else {
                this.current = ["home"];
            }
        }
    },
});

var router = new Router();

React.renderComponent(
    <InterfaceComponent router={router} />,
    document.body
);

Backbone.history.start();