from doctores import acciones

print("""
\n
####### "CONSULTORIO MEDICO" "LEONARDO CONTRERAS MARTINEZ 9 A DSM " #######

""")

hazEl = acciones.Acciones()

def bienvenida():
  
  print("""

  ¿Qué Deseas Hacer?
  \n
  -Registrarte! (Escribe 'registro')
  \n
  -Inicia Sesión (Escribe 'login')
  """)

  accion = input("¿Que Deseas Hacer?:")

  if accion == "registro":
   hazEl.registro()
   bienvenida()

  elif accion == "login":
    hazEl.login()


bienvenida()

