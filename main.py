from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"name": name, "test": test}


#this kind of represents what we call a Json format {key: value}

#register Helloworld as a resource
#if we send get request to /helloworld, it will return Hello World in get function
#<> is to define parameter that I want to be passed in
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")


#start server and start flask application
#debug=True gonna see all of that output and any logging information 
#so if anything wrong we will know why (should be put when develop)
if __name__ == "__main__":
    app.run(debug=True)