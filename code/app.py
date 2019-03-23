from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from users import UserRegister
from pet import Pet, PetsList
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRETAPI_KEY')
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(PetsList, '/pets')
api.add_resource(Pet, '/pet/<string:name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
