# local import
from app.schema import ma, fields

class NoteSchema(ma.SQLAlchemyAutoSchema):
    Id = fields.Integer(attribute='id', dump_only=True)
    Title = fields.Str(attribute='title')
    Body = fields.Str(attribute='body')
    
    class Meta:
        ordered = True
