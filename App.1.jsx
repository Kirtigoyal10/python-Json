import {useEffect} from 'react'
import "./App.css"

 function App() {
  fetch('https://jsonplaceholder.typicode.com/posts').then((result)=>(
    result.json().then((response)=>(
      console.warn (response)

    ))

  )) 
  return (
    <div className="App">
      <h1>Get API Call </h1>
    </div>
  );
    
  }

export default App;
