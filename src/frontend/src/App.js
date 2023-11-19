// App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './index.css';
import Map from './map';
import swift from "./swifttrack.png";


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
    <><div className="divmap">
      <Map coordinates={coordinates}/>
    </div><div className="divmap"
      style={{
        position: 'absolute',
        top: '5%',
        left: '4%',
        zIndex: '1',
        textAlign: 'left',
        color: 'white',
        fontFamily: 'Helvetica',
        fontSize: '11vmin',
        fontWeight: 'bold',
      }}
    >
        Welcome back, Yumeng.
      </div>
      <div
        style={{
          position: 'absolute',
          top: '19%',
          left: '7%',
          zIndex: '1',
          textAlign: 'left',
          color: 'white',
          fontFamily: 'Helvetica',
          fontSize: '5vmin',
          fontWeight: 'bold',
        }}
      >
        We have a package for you to collect.
      </div>
      <div
        style={{
          position: 'absolute',
          top: '89%',
          left: '77%',
          zIndex: '5',
          textAlign: 'left',
        }}>
        <img src={swift} alt= "logo" style={{ width: '300px', height: 'auto' }}/>
      </div>
      </>
    
  );
  
};

export default App;

