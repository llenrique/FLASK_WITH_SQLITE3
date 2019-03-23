import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class PetsList(Resource):
    def get(self):
        return {'pets': pets}


class Pet(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('race', type=str, required=True,
                        help="This field is required")
    parser.add_argument('id', type=int, required=True,
                        help="This field is required")
    parser.add_argument('age', type=int, required=True,
                        help="This field is required")
    parser.add_argument('personality', type=str, required=True,
                        help="This field is required")

    @classmethod
    def find_by_pet_name(cls, name):
        connection = sqlite3.connect('dogcare.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM pets WHERE name=?"
        result = cursor.execute(select_query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {
                'pet': {
                    'id': row[0],
                    'name': row[1],
                    'race': row[2],
                    'age': row[3],
                    'personality': row[4]
                }
            }

    @jwt_required()
    def get(self, name):
        pet = self.find_by_pet_name(name)
        if pet:
            return pet
        return {'message': 'Pet not found'}, 404

    @jwt_required()
    def post(self, name):
        if self.find_by_pet_name(name):
            return ({'message': 'This name has already taken'}, 400)

        data = Pet.parser.parse_args()

        pet = {
            'id': data['id'],
            'name': name,
            'race': data['race'],
            'age': data['age'],
            'personality': data['personality']
        }

        connection = sqlite3.connect('dogcare.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO pets VALUES(NULL, ?, ?, ?, ?)"

        cursor.execute(insert_query, (pet['name'], pet['race'], pet['age'], pet['personality']))

        connection.commit()
        connection.close()

        return pet, 201

    @jwt_required()
    def delete(self, name):
        if self.find_by_pet_name(name):
            connection = sqlite3.connect('dogcare.db')
            cursor = connection.cursor()

            delete_query = "DELETE FROM pets WHERE name=?"

            cursor.execute(delete_query, (name,))

            connection.commit()
            connection.close()

            return {'message': 'Pet deleted'}
        return {'message': 'pet not found for delete'}

    @jwt_required()
    def put(self, name):
        data = Pet.parser.parse_args()
        pet = next(filter(lambda x: x['name'] == name, pets), None)
        if pet is None:
            pet = {
                'id': data['id'],
                'name': name,
                'race': data['race'],
                'age': data['age'],
                'personality': data['personality']
            }
            pets.append(pet)
        else:
            pet.update(data)
        return pet
