import citas.cita as modelo

class Acciones:

    def crear(self, doctor):
        print(f"OK {doctor[1]}, Se creara una nueva consulta")

        paciente = input("Introduce el nombre del paciente: ")
        descripcion = input("Escribe la descripcion de la cita/consulta: ")
        horaAtencion = input("Escribe El horario de antencion: ")
        costo = input("Escribe el costo: ")
        cita = modelo.Cita(doctor[0], paciente, descripcion, horaAtencion, costo)
        guardar = cita.guardar()

        if guardar[0] >=1:
            print(f"\nPerfecto has Agendado la cita de {paciente}")
        else:
            print(f"\nNo has guardado la cita {doctor[1]}")

    def mostrar(self, doctor):
        print(f"\n{doctor[1]} Estas son tus consultas")
        cita = modelo.Cita(doctor[0])
        citas = cita.listar()
        #print(notas)
        for cita in citas:
            print("\n***********************")
            print(cita[2])
            print(cita[3])
            print("\n***********************")
    
    def modificar(self, doctor):
            print(f"\n{doctor[1]} Editar cita ")
            print("Introduca los nuevos datos")

            Paciente = input("Introduce el nombre del paciente: ")
            Descripcion = input("Escribe la descripcion de la cita/consulta: ")
            HoraAtencion = input("Escribe El horario de antencion: ")
            Costo = input("Escribe el costo: ")
            cita = modelo.Cita(doctor[0], Paciente, Descripcion, HoraAtencion, Costo)
            modificar = cita.modificar()
            

            
    def borrar(self, doctor):
            print(f"\n{doctor[1]} !!!Estar por Borrar alguna cita !!!")

            paciente = input("Introduce el nombre del paciente ")
            cita = modelo.Cita(doctor[0], paciente)
            eliminar = cita.eliminar()
            if eliminar[0]>=1:
                print(f"Se borro")
            else:
                print("No se borro la cita, prueba mas tarde")
