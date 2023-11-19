import React, { useEffect } from 'react';
import io from 'socket.io-client';

const SocketComponent = () => {
  useEffect(() => {
    const socket = io('http://localhost:5000', {transports: ['websocket']});

    socket.on('connect', () => {
      console.log('Connected to the server');
      socket.timeout(5000).emit('/api/data', ['GET', 'Truck'] );
    });

    socket.on('message_from_server', (data) => {
      console.log('Received message from server:', data);
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      {/* Render your component content here */}
    </div>
  );
};

export default SocketComponent;