// App.js
import React from 'react';
import Map from './map';

const coordinates = [
  { lat: 37.7749, lng: -122.4194 }, // San Francisco
  { lat: 34.0522, lng: -118.2437 }, // Los Angeles
  // Add more coordinates as needed
];

const App = () => {
  return (
    <div>
      <h1>React Google Maps Example</h1>
      <Map coordinates={coordinates} />
    </div>
  );
};

export default App;