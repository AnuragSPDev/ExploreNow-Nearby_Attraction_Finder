import React, { useState } from 'react';
import './App.css';
import PlaceDetails from './Components/PlaceDetails';
import PlaceSearchForm from './Components/PlaceSearchForm';
import Spinner from './Components/Spinner';
import './styles.css';


function App() {
  const [place, setPlace] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = (data) => {
    console.log('Setting place data:', data);
    setPlace(data);
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>ExploreNow App</h1>
      <PlaceSearchForm onSearch={handleSearch} setLoading={setLoading} />
      { loading ? < Spinner /> : <PlaceDetails place={place} />}
    </div>
  );
}

export default App;
