from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

class ReactController:
    app = None 
    GlobalController = None
    socketio = None

    def __init__(self, global_controller):
        self.GlobalController = global_controller
        self.app = Flask(__name__)
        CORS(self.app)
        self.socketio = SocketIO(self.app)
        self.setup_routes()
        self.app.run(debug=True)

    def setup_routes(self):
        self.app.route('/api/data', methods=['GET'])(self.get_data)

    def get_data(something):
        print(something)
        data = {'message': 'Hello from Flask!'}
        response = jsonify(data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
