from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'key': 'value'}

api.add_resource(HelloWorld, '/vix')

if __name__ == '__main__':
    app.run(debug=True)
