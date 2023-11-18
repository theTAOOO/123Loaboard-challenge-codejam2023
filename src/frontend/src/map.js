// Map.js
import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const Map = ({ coordinates }) => {
  const [map, setMap] = useState(null);

  const mapStyles = {
    height: '400px',
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

  return (
    <LoadScript
      googleMapsApiKey="AIzaSyDRTv4qJaBOqG-pA6yPYKbykJIjQ37bYjs"
      libraries={['places']}
    >
      <GoogleMap
        mapContainerStyle={mapStyles}
        center={defaultCenter}
        zoom={13}
        onLoad={onLoad}
      >
        {coordinates.map((coord, index) => (
          <Marker
            key={index}
            position={{ lat: coord.lat, lng: coord.lng }}
          />
        ))}
      </GoogleMap>
    </LoadScript>
  );
};

export default Map;
