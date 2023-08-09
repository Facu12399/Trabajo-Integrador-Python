class Veterinaria():
    def __init__(self, listado: list) -> None:
        self.__listado = listado
    
    def setPaciente(self,paciente):
        paciente = input("Ingrese el nombre del paciente a agregar: ")
        self.__listado.append(paciente)
        print("Se ha agregado con exito el paciente en la lista")

    def deletePaciente(self,eliminado):
        print(self.__listado)
        eliminado = input("Ingrese el nombre del paciente que desea borrar: ")
        self.__listado.remove(eliminado)
        print("Se ha eliminado con exito al paciente " + eliminado + " de la lista")
    
    def getListado(self):
        return f"La lista de pacientes es: {self.__listado}"

    def __str__(self) -> str:
        cantidad = len(self.__listado)
        return f'El número de pacientes es {cantidad}'
    