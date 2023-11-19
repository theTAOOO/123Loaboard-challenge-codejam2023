from flask import Flask
from flask_socketio import SocketIO

class ReactController:
    app = None 
    GlobalController = None
    socketio = None

    def __init__(self, global_controller):
        self.GlobalController = global_controller
        self.app = Flask(__name__)
        # CORS(self.app)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*", logger=True, engineio_logger=True)
        self.setup_routes()

    def start_thread(self):
        self.app.run(debug=False)
        self.socketio.emit('message_from_server', 'Hello from the server!')

    def setup_routes(self):
        self.app.route('/', methods=['GET'])(self.get_data)
        self.app.route('/get_data', methods=['GET'])(self.get_data)
        self.app.route('/api/data', methods=['GET'])(self.get_data)
        self.socketio.on('message_from_client')(self.handle_message)
        self.socketio.on('connect')(self.say_hello)

    def get_data(message):
        print(message)
        data = {'message': 'Hello from Flask!'}
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    def handle_message(self, message):
        print('Received message:', message)
        self.socketio.emit('message_from_server', message)

    def say_hello(self):
        print('Client connected')
        self.socketio.emit('welcome_message', 'Welcome to the Socket.IO server!') 
    
