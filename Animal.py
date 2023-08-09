
class Animal():
    def __init__(self, nombre: str, edad: str) -> None:
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self) -> str:
        return f'El nombre del paciente es {self.__nombre} y tiene {self.__edad} años'