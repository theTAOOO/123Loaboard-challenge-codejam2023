// App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Map from './map';

const coordinates = [
  { lat: 37.7749, lng: -122.4194 }, // San Francisco
  { lat: 34.0522, lng: -118.2437 }, // Los Angeles
  // Add more coordinates as needed
];

const App = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    axios.get('http://localhost:5000/api/data')
        .then(response => {
            setData(response.data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}, []);

  return (
    <div>
      <Map coordinates={coordinates} title="Welcome back, Yumeng." />
    </div>
  );
};

export default App;