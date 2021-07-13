from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from models.persona import PersonaSchema, personaFisicaSchema
from personasHelper import MetodoPersona

app = Flask(__name__)
api = Api(app)
CORS(app)

class Persona(Resource):
    #api-person-get-by-id
    def get(self, id):
        try:
            schema = PersonaSchema()
            newPeople = MetodoPersona()
            data = newPeople.getpersonasByfolio(id)

            if data is None:
                response = {
                    "Code": 200,
                    "Msg": "Success",
                    "Error": False,
                    "data": {}
                }
            else:
                response = {
                    "Code": 200,
                    "Msg": "Success",
                    "Error": False,
                    "data": schema.dump(data)
                }
        except Exception as e:
            response = {
                "Code": 500,
                "Msg": str(e),
                "Error": True,
                "data": {}
            }

        return response
    
    #person-post
    def post(self):
        response = {}
        try:
            json_data = request.get_json(force=True)
            schema = PersonaSchema()
            data_request = schema.load(json_data)

            nombre = data_request["nombre"]
            entidadFederativa = data_request["entidadFederativa"]
            municipio = data_request["municipio"]

            nuevaPersona = {
                "nombre": nombre,
                "entidadFederativa": entidadFederativa,
                "municipio": municipio,
                "estado": 1
            }
            
            newPeople = MetodoPersona()
            data = newPeople.agregarPersona(nuevaPersona)

            response = {
                "Code": 200,
                "Msg": "Success",
                "Error": False,
                "data": schema.dump(data)
            }
        except Exception as e:
            response = {
                "Code": 500,
                "Msg": str(e),
                "Error": True,
                "data": {}
            }

        return response
    
    #person-update
    def put(self, id):
        response = {}
        try:
            json_data = request.get_json(force=True)
            schema = PersonaSchema()
            data_request = schema.load(json_data)

            nombre = data_request["nombre"]
            entidadFederativa = data_request["entidadFederativa"]
            municipio = data_request["municipio"]

            actualizarPersona = {
                "nombre": nombre,
                "entidadFederativa": entidadFederativa,
                "municipio": municipio,
                "estado": 1
            }
            
            newPeople = MetodoPersona()
            data = newPeople.actualizarPersona(id,actualizarPersona)

            response = {
                "Code": 200,
                "Msg": "Success",
                "Error": False,
                "data": schema.dump(data)
            }
        except Exception as e:
            response = {
                "Code": 500,
                "Msg": str(e),
                "Error": True,
                "data": {}
            }

        return response


class PersonasLista(Resource):
    #api-people-get-all
    def get(self):
        try:

            newPeople = MetodoPersona()
            data = newPeople.getAllpersonas() 

            schema = PersonaSchema(many=True)

            if data is None:
                response = {
                    "Code": 200,
                    "Msg": "Success",
                    "Error": False,
                    "data": {}
                }
            else:
                response = {
                    "Code": 200,
                    "Msg": "Success",
                    "Error": False,
                    "data": schema.dump(data)
                }
        except Exception as e:
            response = {
                "Code": 500,
                "Msg": str(e),
                "Error": True,
                "data": {}
            }

        return response
    
class PersonStatus(Resource):
    #api-person-delete
    def put(self, id):
        response = {}
        try:
            schema = PersonaSchema()
            newPeople = MetodoPersona()
            data = newPeople.eliminarPersona(id) 

            response = {
                "Code": 200,
                "Msg": "Success",
                "Error": False,
                "data": schema.dump(data)
            }
        except Exception as e:
            response = {
                "Code": 500,
                "Msg": str(e),
                "Error": True,
                "data": {}
            }

        return response

# Lectura de personas
api.add_resource(PersonasLista,'/personas/get',endpoint="api-person-get", methods=["GET"])

api.add_resource(Persona,'/personas/<string:folio>',endpoint="api-person-by-id", methods=['GET'])

# Crear personas
api.add_resource(Persona,'/personas',endpoint="api-person-post", methods=["POST"])

# Actualizar personas
api.add_resource(Persona,'/personas/<string:folio>',endpoint="api-person-upate", methods=["PUT"])

# Borrar personas
api.add_resource(PersonStatus,'/personas/status/<string:folio>',endpoint="api-person-status", methods=["PUT"])
  

if __name__ == "__main__":
    app.run(debug=True)