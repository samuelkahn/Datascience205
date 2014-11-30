/** @jsx React.DOM */
var React = require('react');
var request = require('browser-request');

var Button = require('react-bootstrap').Button;
var Input = require('react-bootstrap').Input;
var Table = require('react-bootstrap').Table;

var constants = require('./constants');

var urls = require('./urls');

var YearZip = React.createClass({
    propTypes: {
        action: React.PropTypes.func.isRequired
    },
    handleSubmit: function() {
        var year = this.refs.year.getValue();
        var zip = this.refs.zip.getValue();
        this.action(year, zip);
    },
    render: function() {
        var yearOptions = [];
        for (var i = constants.MIN_YEAR; i <= constants.MAX_YEAR; i++) {
            yearOptions.push(
                <option key={i} value={i}>{i}</option>
            );
        }
        return (
            <form
                className="form-horizontal"
                onSubmit={this.handleSubmit} >
                <Input
                    type="select"
                    ref="year"
                    name="year"
                    label="Year"
                    labelClassName="col-xs-2"
                    wrapperClassName="col-xs-10">
                    {yearOptions}
                </Input>
                <Input
                    type="text"
                    ref="zip"
                    name="zip"
                    label="ZIP Code"
                    labelClassName="col-xs-2"
                    wrapperClassName="col-xs-10">
                </Input>
                <Input
                value="Chose"
                type="submit"
                className="btn-success"
                wrapperClassName="col-xs-offset-2 col-xs-2"/>
            </form>
        );
    }
});

module.exports = YearZip;
