from ast import alias
from statistics import mode
import doctores.doctor as modelo
import citas.acciones
from datetime import datetime

class Acciones:
    def registro(self):
        print("Registrate en el sistema")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        noConsultorio = input("Numero de consultorio: ")
        email = input("Email: ")
        password = input("Introduce una contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, noConsultorio, email, password)
        registro = doctor.registrar()

        if registro[0] >= 1:
            print(f"\nBienvenido {registro[1].nombre} te has registrado Correctamente")
        else:
            print("\nNo se pudo registrar")

           
    def login(self):
       print("\nLOGIN: Identificate en el sistema...")
      
       try: 
           email = input("Introduce tu email: ")
           password = input("Introduce tu contraseña: ")

           doctor = modelo.Doctor('', '', '', email, password)
           login = doctor.identificar()
           now = datetime.now()
           if email == login[4]:
                print(f"Bienvenido {login[1]}, ingresaste en la fecha: {now}")
                self.proximasAcciones(login)


       except Exception as e:
          print("login incorrecto intentelo mas tarde")


    def proximasAcciones(self, doctor):
        print("""
        Aciones disponibles 
         -Agendar cita (crear)
         -Mostar citas (mostar)
         -Modificar cita (modificar)
         -Eliminar cita (eliminar)
         Salir (salir)
        """)
        accion = input("¿Que quieres hacer? ")
        hazEL = citas.acciones.Acciones()

        if accion == "crear":
            hazEL.crear(doctor)
            self.proximasAcciones(doctor)

        elif accion == "mostar":
            hazEL.mostrar(doctor)
            self.proximasAcciones(doctor)
        
        elif accion == "modificar":
            hazEL.mostrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "eliminar":
            hazEL.borrar(doctor)
            self.proximasAcciones(doctor)

        elif accion == "salir":
            exit()
    
    
