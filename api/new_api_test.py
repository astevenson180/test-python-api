from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {
            "data":"Hello world"
        }

api.add_resource(HelloWorld, "/helloworld")


if __name__ == "__main__":
    app.run(debug = True) #only using debug= true in development environment to see output


