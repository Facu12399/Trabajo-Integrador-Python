class Veterinaria():
    def __init__(self, listado: list) -> None:
        self.__listado = listado
    
    def setPaciente(self,paciente):
        paciente = input("Ingrese el nombre del paciente a agregar: ")
        self.__listado.append(paciente)
        return "Se ha agregado con exito el paciente en la lista"

    def deletePaciente(self,eliminado):
        print(self.__listado)
        eliminado = input("Ingrese el nombre del paciente que desea borrar: ")
        self.__listado.remove(eliminado)
        return f"Se ha eliminado con exito al paciente {eliminado} de la lista"
    
    def getListado(self):
        return f"La lista de pacientes es: {self.__listado}"

    def __str__(self) -> str:
        cantidad = len(self.__listado)
        return f'El número de pacientes es {cantidad}'
        

class Animal():
    def __init__(self, nombre: str, edad: str) -> None:
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self) -> str:
        return f'El nombre del paciente es {self.__nombre} y tiene {self.__edad} años'
    
class Paciente(Animal):
    def __init__(self, nombre: str, edad: str) -> None:
        super().__init__(nombre, edad)

lista = []

hola = Veterinaria(lista)

hola2 = Animal("Facundo","24")

print(hola2)