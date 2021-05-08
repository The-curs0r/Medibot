import React from 'react';
import {Form,Button,ButtonGroup} from 'react-bootstrap'
import './Symptom.css'
class Symptom extends React.Component {

	constructor(props) {
        super(props);
        this.state = {
			sevValue: 0
        };
		this.updateSymptom = this.updateSymptom.bind(this);
    }

    updateSymptom() {
		this.props.updateSymptom(this.props.index,this.state.sevValue);
	}

	updateValue(event,value) {
		this.setState({sevValue:value},function(){
			this.updateSymptom()
		})
	}

    render(){
		const elements = ['Headache', 'Back Pain', 'Chest Pain','Cough','Low Body Temp','Fever'];
        return (
			<div className="Maina">
				<Form.Check aria-label="option 1" onChange={(e)=>this.updateValue(e,this.state.sevValue?0:1)}/>
				{this.state.sevValue && elements.includes(this.props.name)?
				<ButtonGroup aria-label="Basic example">
					<Button variant={this.state.sevValue^1?"secondary":"success"} onClick={(e)=>this.updateValue(e,1)}>Low</Button>
					<Button variant={this.state.sevValue^2?"secondary":"success"} onClick={(e)=>this.updateValue(e,2)}>Medium</Button>
					<Button variant={this.state.sevValue^3?"secondary":"success"} onClick={(e)=>this.updateValue(e,3)}>Severe</Button>
				</ButtonGroup>
:null}
				<label className="diseaseName">{this.props.name}</label>
			</div>
		)
    }
}

export default Symptom;