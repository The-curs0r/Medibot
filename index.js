const express = require('express');
const {spawn} = require('child_process');
const path = require('path');
const app = express();

app.get('/api/test', (req, res) => {
	res.send('Test backend!')
})
app.get('/api/py', (req, res) => {
	disease_flags = (req.query.dis)
	console.log(disease_flags)
	var dataToSend;
	var largeDataSet = [];
	const python = spawn('python', ['bot/engine.py',disease_flags[0],disease_flags[01],disease_flags[02],disease_flags[03],disease_flags[04],disease_flags[05],disease_flags[06],disease_flags[07],disease_flags[08],disease_flags[9],disease_flags[10],disease_flags[11],disease_flags[12]]);
//Headache backp chestp  cough fainting fatigue sunkeneye lowbodytemp resetles sorethro fever nausea blurvis
	python.stdout.on('data', function (data) {
		console.log('Pipe data from python script ...');
		largeDataSet.push(data);
		dataToSend=data.toString();	
	});
	python.on('close', (code) => {
		console.log(`child process close all stdio with code ${code}`);
		console.log(largeDataSet)
		//res.send(largeDataSet[0].data)
		res.send(dataToSend)
	});	
   })
const port = process.env.PORT || 8080;
app.listen(port);
console.log('App is listening on port ' + port);