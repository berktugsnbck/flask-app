from flask import Flask
from flask_restful import Resource, Api
import sys
import json


app = Flask(__name__)
api = Api(app)

if sys.argv.__len__() > 1:
	port = sys.argv[1]

class HelloWorld(Resource):
	def get(self):

		return json.dumps({"Message":"ok"})
		

api.add_resource(HelloWorld, '/db')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5001)

