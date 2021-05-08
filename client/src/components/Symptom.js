import React from 'react';
import {Form} from 'react-bootstrap'
import './Symptom.css'
class Symptom extends React.Component {

	constructor(props) {
        super(props);
        this.state = {
        };
		this.updateSymptom = this.updateSymptom.bind(this);
    }

    updateSymptom( event ) {
		this.props.updateSymptom(this.props.index);
	}

    render(){
        return (
			<div className="Maina">
				<Form.Check aria-label="option 1" onChange={(e)=>this.updateSymptom(e)}/>
				<label>{this.props.name}</label>
			</div>
		)
    }
}

export default Symptom;