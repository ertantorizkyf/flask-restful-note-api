# local import
from app.models import db, datetime
from app.schema.note import NoteSchema as Schema
from app.models.timestamp import TimestampModel

class NoteModel(db.Model, TimestampModel):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(255))
    body = db.Column(db.Text, nullable=False)
    
    @classmethod
    def getAll(cls):
        notes = cls.query.filter(cls.deleted_date == None).order_by(cls.id.desc()).all()
        result = cls.dumpIntoSchema(notes, isMany=True)
        return result
    
    @classmethod
    def getById(cls, id):
        return cls.query.filter(cls.id == id, cls.deleted_date == None).first()
    
    def insert(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        self.deleted_date = datetime.utcnow()

    def dumpIntoSchema(self, isMany = False):
        result = Schema(many = isMany).dump(self)
        return result
