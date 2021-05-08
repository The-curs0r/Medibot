import axios from 'axios';
import './mediBot.css';
import Symptom from './Symptom'
import React, { Component } from 'react';
import {Button } from 'react-bootstrap';

class mediBot extends Component {
	constructor() {
		super();
		this.state = {
				symptoms: [0,0,0,0,0,0,0,0,0,0,0,0,0],
				fever:0,
				fever_sev:null,
				back_pain :0,
				back_pain_sev:null,
				chest_pain :0,
				chest_pain_sev :null,
				cough :0,
				cough_sev :null,
				fainting :0,
				fainting_sev :null,
				sore_throat :0,
				sore_throat_sev :null,
				fatigue :0,
				fatigue_sev  :null,
				low_body_temp :0,
				low_body_temp_sev :null,
				sunken_eyes :0,
				sunken_eyes_sev :null,
				nausea :0,
				nausea_sev :null,
				blurred_vision :0,
				blurred_vision_sev :null,
				headache :0,
				headache_sev :null,
				restlessness :0,
				restlessness_sev :null,
				disease:null
		};
	}
	predictDisease = () => {
		axios.get('/api/py',{
			params: {
				dis: this.state.symptoms
//Headache backp chestp  cough fainting fatigue sunkeneye lowbodytemp resetles sorethro fever nausea blurvis
			}
		  })
		.then((response) => {
			this.setState({disease:response.data},function() { console.log(this.state.disease) })
		})
	}
	updateSymptom = (index) => {
		var ind = index ;
		var symptomsUpdated = this.state.symptoms;
		symptomsUpdated[ind] = symptomsUpdated[ind]===0?1:0;
		this.setState({symptoms:symptomsUpdated},function() { console.log(this.state.symptoms[ind]) });
	}
render(){
	const elements = ['Headache', 'Back Pain', 'Chest Pain','Cough','Fainting','Fatigue','Sunken Eyes','Low Body Temp','Restlessness','Sore Throat','Fever','Nausea','Blurred Vision'];
	return (
		<div className="Main">
			<div className="Symptoms">
				{elements.map((type,index) => (
					<Symptom updateSymptom={this.updateSymptom} name={type} index={index} key={index} />
				))}
			</div>
			<Button variant="dark" onClick={this.predictDisease}>Estimate Disease</Button>
		</div>
	);

}
		
}
export default mediBot;
