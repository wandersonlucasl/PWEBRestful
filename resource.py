from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Tutor, Pet, TutorSchema, PetSchema

class TutorResource(Resource):
    def get (self, tutor_id=None):
        if tutor_id is None:
            tutors = Tutor.query.all()
            return TutorSchema(many=True).dump(tutors), 200

        tutor = Tutor.query.get(tutor_id)
        return TutorSchema().dump(tutor), 200

    def post (self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome_tutor', type=str, required=True)
        args = parser.parse_args()
        tutor = Tutor(nome=args['nome_tutor'])
        db.session.add(tutor)
        db.session.commit()
        return TutorSchema().dump(tutor), 201

    def delete (self, tutor_id):
        parser = reqparse.RequestParser()
        parser.add_argument('tutor_id', type=int, required=True)
        args = parser.parse_args()
        tutor = Tutor.query.get(args['tutor_id'])
        db.session.delete(tutor)
        db.session.commit()
        return 'tutor has deleted', 204


class PetResource (Resource):
    def get (self, pet_id):
        pet = Pet.query.get(pet_id)
        return PetSchema().dump(pet), 200
        
