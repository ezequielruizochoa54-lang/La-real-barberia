from conexion import ConexionDB

class DPersona:
    def __init__(self):
        self.__db = ConexionDB().conexionSupabase()
        self.__nombreTabla = 'Persona'

    def __ejecutarConsultas(self, consulta, tipoConsulta = None):
        try:
            if tipoConsulta == 'SELECT':
                resultado = consulta.execute().data
                return resultado
            else:
                resultado = consulta.execute()
                return resultado
        except Exception as e:
            raise e

    def mostrarPersonas(self):
        consulta = self.__db.table(self.__nombreTabla).select('*')
        return self.__ejecutarConsultas(consulta, 'SELECT')

    def nuevaPersona(self, persona: dict):
        consulta = self.__db.table(self.__nombreTabla).insert(persona)
        return self.__ejecutarConsultas(consulta)

    def actualizarPersona(self, persona:dict, docidentidad: str):
        consulta = self.__db.table(self.__nombreTabla).update(persona).eq('docidentidad', docidentidad)
        return self.__ejecutarConsultas(consulta)

    def eliminarPersona(self, docidentidad: str):
        consulta = self.__db.table(self.__nombreTabla).delete().eq('docidentidad', docidentidad)
        return self.__ejecutarConsultas(consulta)