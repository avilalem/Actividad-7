def registrar_estudiantes(estudiantes):
    try:
        cantida=int(input("Cuantos estudiantes desea registrar?:"))
    except ValueError:
        print("Ingrese un numero valido")
        return

    for _ in range(cantida):
        print("Registrando estudiante...")
        carnet=input("Carnet: ").stringp()
        if carnet in estudiantes:
            print("El carnet ingresado ya existe. Intente nuevamente")
            continue
        nombre=input("Nombre Completo: ")
        try
            edad=int(input("Edad: "))
        except ValueError:
            print("Ingrese un numero valido")
            return
        carrera=input("Carrera: ")
        try

def menu():
    sistema=SistemaEstudiante()
    while true:
        print("\n ___ Menu ___")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estuiantes y cursos")
        print("3. Buscar estuiante por carnet")
        print("4. Salir")