import React, { useEffect } from 'react';
import io from 'socket.io-client';

const SocketComponent = () => {
  useEffect(() => {
    const socket = io('http://localhost:5000', {transports: ['websocket']});

    socket.on('connect', () => {
      console.log('Connected to the server');
      socket.timeout(5000).emit('/api/data', ['GET', 'TRUCK'] );
    });

    socket.on('message_from_server', (data) => {
      if ('SET' == data[0]) {
        handleServerSetMessage(data);
      } else if ('UPD' == data[0]) {
        handleServerUpdMessage(data);
      }
    });

    // TODO: PICKUP LOAD
    // const sendMessageToServer = () => {
    //   // Emit a custom event to the server with the messageToSend data
    //   socket.emit('send_message_to_server', messageToSend);
    // };

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

const PickUpLoad = (load_id) => {

}

const handleServerSetMessage = (data) => {
  console.log('Received Set from server:', data);
  if ('TRUCK' == data[1]) {
    // SetEmulatedTruck(data[2]);
  } else if ('LOAD' == data[0]) {
    // AddLoad(data[2]);
  }
};

const handleServerUpdMessage = (data) => {
  console.log('Received UPD from server:', data);
  // UpdateEmulatedTruck(data[2])
};

export default SocketComponent;