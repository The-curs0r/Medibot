
import './App.css';
import axios from 'axios'
function App() {
	const hitBackend = () => {
		axios.get('/api/test')
		.then((response) => {
		console.log(response.data)
		})
		}
  return (
    <div className="App">
	  <button onClick={hitBackend}>Send request</button>
    </div>
  );
}

export default App;
