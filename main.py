from Paciente import Paciente
from funciones import nuevoPaciente,quitarPaciente,listarPacientes,nuevaConsulta,obtenerDetallePaciente

def progPrincipal():
    print("¡Bienvenido al sistema online del veterinario!\n")
    print("¿Qué desea realizar?\n")
    
    lista = []
    opcion = None
    paciente1 = None
    paciente2 = None
    paciente3 = None
    consulta1 = []
    consulta2 = []
    consulta3 = []

    while(opcion != 7):

        opcion = int(input("1-Ver la lista de pacientes.\n2-Ver detalles del paciente.\n3-Cargar nuevo paciente\n4-Quitar paciente\n" +
          "5-Cargar consulta\n6-Dar alta de tratamiento medico.\n7-Salir\n\nElija la opcion que desea realizar: "))
        print("\n")

        if opcion == 1:
            if len(lista) == 0:
                print("No hay pacientes en la base de datos\n")
            else:
                i = 1
                print("Lista de pacientes")
                for list in lista:
                    print(f"{i}) {list.getNombre()}")
                    i = i + 1
                print("\n")
        elif opcion == 2:
            if len(lista) == 0:
                print("No hay pacientes en la base de datos\n")
            else:
                i = 1
                print("Lista de pacientes")
                for list in lista:
                    print(f"{i}- {list.getNombre()}")
                    i = i + 1
                print("\n")
                elegir = int(input("Elija el nro de paciente para conocer sus datos: "))
                if elegir == 1 :
                    print(paciente1.getDatos())
                
                if elegir == 2:
                    print(paciente2.getDatos())

                if elegir == 3:
                    print(paciente3.getDatos())
        elif opcion == 3:
            nombre = input("Ingrese el nombre del paciente a agregar: ")
            edad = input("Ingrese la edad del paciente a agregar: ")
            raza = input("Ingrese la raza del animal: ")
            print("\n")

            if paciente1 == None:
                paciente1 = nuevoPaciente(nombre,edad)
                paciente1 = Paciente(nombre,edad,raza,consulta1,False)
                lista.append(paciente1)
                print("Se agrego con exito el paciente\n")
            elif paciente2 == None:
                paciente2 = nuevoPaciente(nombre,edad)
                paciente2 = Paciente(nombre,edad,raza,consulta2,False)
                lista.append(paciente2)
                print("Se agrego con exito el paciente\n")
            else:
                paciente3 = nuevoPaciente(nombre,edad)
                paciente3 = Paciente(nombre,edad,raza,consulta3,False)
                lista.append(paciente3)
                print("Se agrego con exito el paciente\n")

        elif opcion == 4:
            if len(lista) == 0:
                print("No hay pacientes para eliminar\n")
            else:
                i = 1
                print("Lista de pacientes")
                for list in lista:
                    print(f"{i}- {list.getNombre()}")
                    i = i + 1
                print("\n")
                eliminar = int(input("Ingrese el número del paciente a eliminar: "))
                print(quitarPaciente(lista,eliminar-1))
                print("\n")

        elif opcion == 5:
            if len(lista) == 0:
                print("No hay pacientes para agregar consulta\n")
            else:
                i = 1
                print("Lista de pacientes")
                for list in lista:
                    print(f"{i}- {list.getNombre()}")
                    i = i + 1
                print("\n")
                n = int(input("Ingrese el número del paciente para agregar consulta: "))
                if n == 1:
                    nuevaConsulta(consulta1,"")
                    print("\n")

                if n == 2:
                    nuevaConsulta(consulta2,"")
                    print("\n")

                if n == 3:
                    nuevaConsulta(consulta3,"")
                    print("\n")

        elif opcion == 6:
            if len(lista) == 0:
                print("No hay pacientes para agregar consulta\n")
            else:
                i = 1
                print("Lista de pacientes")
                for list in lista:
                    print(f"{i}- {list.getNombre()}")
                    i = i + 1
                print("\n")
                n = int(input("Ingrese el número del paciente para dar el alta medica: "))
                if n == 1:
                    paciente1 = Paciente(nombre,edad,raza,consulta1,True)
                    print("El paciente fue dado de alta.\n")
                    lista.pop(0)

                if n == 2:
                    paciente2 = Paciente(nombre,edad,raza,consulta2,True)
                    print("El paciente fue dado de alta.\n")
                    lista.pop(1)

                if n == 3:
                    paciente3 = Paciente(nombre,edad,raza,consulta3,True)
                    print("El paciente fue dado de alta.\n")
                    lista.pop(2)

        elif opcion == 7:
            break
        else:
            print("Opcion incorrecta\n")

    print("Gracias por utilizar el sistema.")    

progPrincipal()