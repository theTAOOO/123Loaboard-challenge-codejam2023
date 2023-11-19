from flask import Flask
from flask_socketio import SocketIO

class ReactController:
    app = None 
    global_controller = None
    socketio = None

    def __init__(self, global_controller):
        self.global_controller = global_controller
        self.app = Flask(__name__)
        # CORS(self.app)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", logger=True, engineio_logger=True)
        self.setup_routes()

    def start_thread(self):
        self.app.run(debug=False)
        self.socketio.emit('message_from_server', 'Hello from the server!')

    def setup_routes(self):
        self.socketio.on('/api/data')(self.global_controller.MessageHandler.HandleFEIncomingMessage)
        self.socketio.on('message_from_client')(self.handle_message)
        self.socketio.on('connect')(self.say_hello)

    def handle_message(self, message):
        print('Received message:', message)

    def say_hello(self):
        print('Client connected')
        self.socketio.emit('message_from_server', 'Welcome to SwiftTrack!')
    
    def send_msg(self, load):
        self.socketio.emit('message_from_server', load)
