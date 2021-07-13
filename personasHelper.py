from flask import Flask, jsonify, request

class MetodoPersona():
    
    personas = []
    
    def __init__(self):
        self.personas = [
        {
            "id" : 1,
            "nombre" : "Gerardo",
            "entidadFederativa": "Guanajuato",
            "municipio" : "León",
            "estado" : 1
        },
        {
            "id" : 2,
            "nombre" : "Maria",
            "entidadFederativa": "Guanajuato",
            "municipio" : "León",
            "estado" : 1
        },
        {
            "id" : 3,
            "nombre" : "Rodrigo",
            "entidadFederativa": "Jalisco",
            "municipio" : "Guadalajara",
            "estado" : 1
        },
        {
            "id" : 4,
            "nombre" : "Aarón",
            "entidadFederativa": "Michoacán",
            "municipio" : "La Piedad",
            "estado" : 1
        },
        {
            "id" : 5,
            "nombre" : "Maria",
            "entidadFederativa": "Chihuahua",
            "municipio" : "Chihuahua",
            "estado" : 1
        },
        {
            "id" : 6,
            "nombre" : "Maria",
            "entidadFederativa": "Nuevo león",
            "municipio" : "Monterrey",
            "estado" : 1
        },
        {
            "id" : 7,
            "nombre" : "Gerardo",
            "entidadFederativa": "Guanajuato",
            "municipio" : "León",
            "estado" : 1
        },
        {
            "id" : 8,
            "nombre" : "Maria",
            "entidadFederativa": "Guanajuato",
            "municipio" : "León",
            "estado" : 1
        },
        {
            "id" : 9,
            "nombre" : "Gabriel",
            "entidadFederativa": "Veracruz",
            "municipio" : "Xalapa",
            "estado" : 1
        },
        {
            "id" : 10,
            "nombre" : "Maria",
            "entidadFederativa": "Querétaro",
            "municipio" : "Querétaro",
            "estado" : 1
        }
        ]
    
    def ObtenerMasRepetido(self,list_persona):
        result = None
        repetido = []
        unico = []
        
        if len(list_persona) > 0:
            for persona in list_persona:
                if persona["nombre"] not in unico:
                    unico.append(persona["nombre"])
                else:
                    if persona["nombre"] not in repetido:
                        repetido.append(persona["nombre"])
                        
        if len(repetido) > 0:
            result = repetido[0]
            
        return result
    
    def getAllpersonas(self):
        return self.personas
    
    def getpersonasByid(self, id):
        result = next((persona for persona in self.personas if persona["id"] == id), None)
        
        return result
    
    def agregarPersona(self, nuevaPersona):
        tamanio = len(self.personas)
        nuevaPersona["id"] = tamanio + 1
        self.personas.append(nuevaPersona)
        
        return nuevaPersona
    
    def eliminarPersona(self, id):
        personaFound = None
        for persona in self.personas:
            if persona["id"] == id:
                personaFound = persona
                self.personas.pop(persona)

        return personaFound
    
    def actualizarPersona(self, id, actualizarPersona):
        
        personaActualizada = None

        for persona in self.personas:
            if persona["id"] == id:
                personaActualizada = actualizarPersona
                self.personas[id] = actualizarPersona
        
        return personaActualizada