from Animal import Animal

class Paciente(Animal):
    def __init__(self, nombre: str, edad: str, raza: str, consultas: list, pctm: bool) -> None:
        super().__init__(nombre,edad)
        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.__consultas = consultas
        self.pctm = pctm
        pctm = False

    def __str__(self) -> str:
        cantconsul = len(self.__consultas)
        return f'La raza del animal es {self.__raza} y la cantidad de consultas que hizo fue {cantconsul}'
    
    def setConsulta(self,consulta):
        consulta = input("Ingrese la consulta que desea agregar: ")
        self.__consultas.append(consulta)
        print("Se ha agregado con exito su consulta")

    def getDatos(self):
        return f'\nDatos del paciente\nNombre: {self.__nombre}\nEdad: {self.__edad}\nRaza: {self.__raza}\nConsultas: {self.__consultas}\n'
    
    def getNombre(self):
        return f'{self.__nombre}'


