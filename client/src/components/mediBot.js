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
	updateSymptom = (index, value) => {
		var ind = index ;
		var symptomsUpdated = this.state.symptoms;
		symptomsUpdated[ind] = value;
		this.setState({symptoms:symptomsUpdated},function() { console.log(this.state.symptoms[ind]) });
	}
	searchDisease = (event,value) => {
		let mapsURL = "http://maps.google.com/?q="+value+" doctors near me";
		window.open(encodeURI(mapsURL), "_blank")
	}
	//headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision
render(){
	const elements = ['Headache', 'Back Pain', 'Chest Pain','Cough','Fainting','Fatigue','Sunken Eyes','Low Body Temp','Restlessness','Sore Throat','Fever','Nausea','Blurred Vision'];
	var perfMatch = this.state.disease == null ? null : String(this.state.disease).charAt(0)
	let [first, ...rest] = String(this.state.disease).substring(1).split('.')
	rest = rest.join('.')
	return (
		<div className="Main">
			<h1>
				Mark your symptoms and their severity
			</h1>
			<div className="Symptoms">
				{elements.map((type,index) => (
					<Symptom updateSymptom={this.updateSymptom} name={type} index={index} key={index} />
				))}
			</div>
			<Button className="btnEstimate" variant="light" onClick={this.predictDisease}>Match Disease</Button>
			{this.state.disease == null ? null : <div className="resultsDiv">
				<h2>
				{
					( perfMatch === "0" ? "You don't have any symptoms and are perfectly healthy.":
					perfMatch==="1"? "Your symptoms match "+first:
						"You might be suffering from "+first) }
				</h2>
				{
					perfMatch === "0" ? null:
					<div>
					<p className="resultsDivText">
						{rest}
					</p>
					{<Button variant="light" onClick={(e)=>this.searchDisease(e,first)}>Search for {first} doctors near you</Button>}
					</div>
				}
			</div>}
		</div>
	);
}
}
export default mediBot;
