
import './App.css';
import Header from './components/Header.js';
import Home from './components/Home';
import mediBot from './components/mediBot';
import {BrowserRouter,Route} from 'react-router-dom';
function App() {
	
	return (
		<BrowserRouter>
			<Header />
			<Route exact path="/" component={Home} />
			<Route exact path="/medibot" component={mediBot} />
		</BrowserRouter>
		);
}

export default App;
