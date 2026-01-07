from capaDatos.dPersona import DPersona

class NPersona:
    def __init__(self):
        self.__dPersona = DPersona()

    def mostrarPersonas(self):
        return self.__dPersona.mostrarPersonas()

    def nuevaPersona(self, persona: dict):
        self.__dPersona.nuevaPersona(persona)

    def actualizarPersona(self, persona: dict, docidentidad: str):
        return self.__dPersona.actualizarPersona(persona, docidentidad)

    def eliminarPersona(self, docidentidad: str):
        return self.__dPersona.eliminarPersona(docidentidad)