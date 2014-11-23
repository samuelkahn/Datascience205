/** @jsx React.DOM */
var React = require('react');
var request = require('browser-request');

var Table = require('react-bootstrap').Table;

var urls = require('./urls');
var YearZipSelector = require('./YearZipSelector');


var Data = React.createClass({
    propTypes: {
        data: React.PropTypes.object.isRequired
    },
    render: function() {
        return (
            <tr>
                <td>
                    {data.year}
                </td>
                <td>
                    {data.zip}
                </td>
                <td>
                    {data.income}
                </td>
            </tr>
        );
    }
});

var DataList = React.createClass({
    propTypes: {
        data: React.PropTypes.array.isRequired
    },
    getInitialState: function() {
        return {data: []};
    },
    getDatas: function(year, zip) {
        var url = urls.GET.yearZip;
        url += 'year' + '/' + zip;
        var options = {
            url: url,
            method: 'GET'
        };
        request(options, function(err, response, body) {
            this.setState({data: body});
        }.bind(this))
    },
    render: function() {
        var datas = this.state.data.map(function(data) {
            return (<Data data={data} />);
        });
        return (
            <div>
                <Table striped bordered condensed hover>
                    <thead>
                        <th>Year</th>
                        <th>Zip</th>
                        <th>Income</th>
                    </thead>
                    <tbody>
                        {datas}
                    </tbody>
                </Table>
                <h3>Enter a Year/Zip to look at</h3>
                <YearZipSelector action={this.getDatas} />
            </div>
        );
    }
});


module.exports = DataList;