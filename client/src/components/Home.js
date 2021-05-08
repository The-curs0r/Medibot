import './Home.css';
import {Button } from 'react-bootstrap';

const Home = ()=>{
	return (
		<div className="HomeDiv">
			<p className="HomeDivHead">Medibot</p>
			<p className="HomeDivHead2">A knowledge-based expert system</p>
			<Button className="btnTry" variant="light" href="/medibot">Try it out!</Button>
		</div>
	  );
}
export default Home;
