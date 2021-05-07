const express = require('express');
const path = require('path');
const app = express();

app.get('/api/test', (req, res) => {
	res.send('Test backend!')
})

const port = process.env.PORT || 8080;
app.listen(port);
console.log('App is listening on port ' + port);