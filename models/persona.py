from marshmallow import Schema, fields, validate

class PersonaSchema(Schema):    
    id = fields.Integer()
    nombre = fields.String(required=True,validate=validate.Length(max=50))
    entidadFederativa = fields.String(required=True,validate=validate.Length(max=30))
    municipio = fields.String(required=True,validate=validate.Length(max=30))   
    estado = fields.Integer()
    
class personaFisicaSchema(PersonaSchema):    
    entidadFederativa = fields.String(required=True,validate=validate.Length(max=30))