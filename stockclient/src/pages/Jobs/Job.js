import React, { Component } from 'react'
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import Button from '@material-ui/core/Button';

export class Job extends Component {

    deleteUser(id){
        const url = '/Job/' + id;
        fetch(url, {
            method: 'POST'
        })
        .then((response) => {
            //this.props.stateRefresh();
        });
        
    }
    render() {
        return (
            <TableRow>
                <TableCell>{this.props.id}</TableCell>
                <TableCell>{this.props.jobname}</TableCell>

                <TableCell><Button variant="contained" color="primary" onClick={(e) => {this.deleteUser(this.props.id)}}>실행</Button></TableCell>
        </TableRow>
        )
    }
}

export default Job

