// Map.js
import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const Map = ({ coordinates, title }) => {
  const [map, setMap] = useState(null);

  const mapStyles = {
    height: '100vh',
    width: '100%',
  };

  const defaultCenter = {
    lat: coordinates[0].lat,
    lng: coordinates[0].lng,
  };

  const onLoad = (map) => {
    setMap(map);
  };

  useEffect(() => {
    if (map) {
      const bounds = new window.google.maps.LatLngBounds();
      coordinates.forEach((coord) => {
        bounds.extend(new window.google.maps.LatLng(coord.lat, coord.lng));
      });
      map.fitBounds(bounds);
    }
  }, [map, coordinates]);

  const mapOptions = {
    fullscreenControl: false, // Disable the fullscreen control
    mapTypeControl: false,
    rotateControl: false, // Disable the rotate control
    scaleControl: false, // Disable the scale control
    panControl: false, // Disable the pan control
    streetViewControl: false,
    zoomControl: false,
  };

  return (
    <LoadScript
      googleMapsApiKey="AIzaSyDRTv4qJaBOqG-pA6yPYKbykJIjQ37bYjs"
      libraries={['places']}
    >
      <GoogleMap
        mapContainerStyle={mapStyles}
        center={defaultCenter}
        zoom={13}
        options={mapOptions}
        onLoad={onLoad}
      >
        {coordinates.map((coord, index) => (
          <Marker
            key={index}
            position={{ lat: coord.lat, lng: coord.lng }}
          />
        ))}
        <div
          style={{
            position: 'absolute',
            top: '5%',
            left: '5%',
            zIndex: '1',
            textAlign: 'left',
            color: 'black',
            fontFamily: 'Helvetica',
            fontSize: '60px',
            fontWeight: 'bold',
          }}
        >
          {title}
        </div>
        <div
          style={{
            position: 'absolute',
            top: '15%',
            left: '7%',
            zIndex: '1',
            textAlign: 'left',
            color: 'black',
            fontFamily: 'Helvetica',
            fontSize: '30px',
            fontWeight: 'bold',
          }}
      >
        We have a package for you to collect.
      </div>
      </GoogleMap>
    </LoadScript>
  );
};

export default Map;
