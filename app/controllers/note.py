# package import
from flask_restful import Resource, reqparse

# local import
from app import db
from app.models.note import NoteModel as Model

class Note(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('title', type=str)
    parser.add_argument('body', type=str, required=True, nullable=False)

    def get(self):
        response = Model.getAll()

        return response, 200
    
    def post(self):
        payload = self.parser.parse_args()

        note = Model(
            title = payload['title'],
            body = payload['body']
        )
        
        try:
            note.insert()
            db.session.commit()
        except:
            db.session.rollback()
            return {'message': 'error while inserting note'}

        response = Model.dumpIntoSchema(note)
        return response, 201


class NoteById(Resource):
    def get(self, id):
        note = Model.getById(id)
        
        if note:
            response = Model.dumpIntoSchema(note)
            return response, 200

        return {'message': 'note with id {} doesn\'t exist'.format(id)}
    
    def put(self, id):
        note = Model.getById(id)
        payload = Note.parser.parse_args()
        
        if note:
            try:
                note.title = payload['title']
                note.body = payload['body']
                db.session.commit()
            except:
                db.session.rollback()
                return {'message': 'error while updating note'}
            
            response = Model.dumpIntoSchema(note)
            return response, 200
        
        return {'message': 'note with id {} doesn\'t exist'.format(id)}
    
    def delete(self, id):
        note = Model.getById(id)
        
        if note:
            try:
                note.delete()
                db.session.commit()
            except:
                db.session.rollback()
                return {'message': 'error while deleting note'}
            
            return {'message': 'delete success'}

        return {'message': 'note with id {} doesn\'t exist'.format(id)}

