from flask import Flask, jsonify
from flask_restx import Resource, Api
from src.config import DevelopmentConfig

# instantiate the app
app = Flask(__name__)
api = Api(app)

# set config
app.config.from_object(DevelopmentConfig)

# new class
class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')
