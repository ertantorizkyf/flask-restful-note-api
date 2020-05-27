# controller import
from app.controllers.note import Note, NoteById

def routes(app, api):
    @app.route('/')
    def index():
        return {'status': 200, 'message': 'OK'}

    api.add_resource(Note, '/note')
    api.add_resource(NoteById, '/note/<int:id>')
