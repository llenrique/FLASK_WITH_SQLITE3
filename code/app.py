from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRETAPI_KEY')
api = Api(app)

# jwt = JWT(app, something, identity)


if __name__ == '__main__':
    app.run(debug=True)
