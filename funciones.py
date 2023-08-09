from Paciente import Paciente


def nuevoPaciente(nombre,edad):  
    paciente = Paciente(nombre,edad,"",[],False)
    return paciente

def quitarPaciente(ListadoPacientes: list, Veterinaria):
    ListadoPacientes.pop(Veterinaria)
    return "Se quito el paciente con exito"

def listarPacientes(ListadoPacientes):
    for i in ListadoPacientes:
        print(i)

def nuevaConsulta(paciente: list,consulta: str):
    consulta = input("Ingrese la consulta del paciente: ")
    paciente.append(consulta)
    print("Se agrego con exito su consulta al paciente ")

def obtenerDetallePaciente(paciente):
    return paciente

ListadoPacientes = []
Consultas = []
