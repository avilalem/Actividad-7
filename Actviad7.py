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
        try:
            edad=int(input("Edad: "))
        except ValueError:
            print("Ingrese un numero valido")
            return
        carrera=input("Carrera: ")
        try:
            num_cursos=int(input("Cuantos cursos desea registrar?: "))
        except ValueError:
            print("Ingrese un numero valido")
            return

        cursos={}
        for i in range (num_cursos):
            print(f"Curso {i+1}:")
            nombre_curso=input("Nombre Curso: ").strip()
            def pedir_nota(titulo):
                while True:
                    nota=float(input("Nota: "))
                    if 0<=nota<=100:
                        return nota
                    else:
                        print("Ingrese un numero valido")
            tarea=pedir_nota("Nota de tarea: ")
            parcial=pedir_nota("Nota de parcial: ")
            proyecto=pedir_nota("Nota de proyecto: ")

            cursos[nombre_curso]={
                "tarea":tarea,
                "parcial":parcial,
                "proyecto":proyecto
            }
        estudiantes[carnet]={
            "nombre":nombre,
            "edad":edad,
            "carrera":carrera,
            "cursos":cursos
        }
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    print("Lista de estudiantes:")
    for carnet, datos in estudiantes.items():
        print(f"Carnet: {carnet} - Nombre: {datos['nombre']} - Edad: {datos['edad']} - Carrera: {datos['carrera']}")
        cursos=datos.get["cursos",{}]
        if cursos:
            for curso, notas in cursos.items():
                print(f"Curso: {curso}")
                print(f"Notas de tarea: {notas['tarea']}")
                print(f"Notas de parcial: {notas['parcial']}")
                print(f"Notas de proyecto: {notas['proyecto']}")
        else:
            print("No tiene cursos registrados ")

def buscar_carnet (estudiantes):
    carnet=input("Ingrese el numero de carnet que desea buscar: ").strip()
    estudiante=estudiantes[carnet]
    if estudiante:
        print(f"Nombre: {estudiante['nombre']} - Edad: {estudiante['edad']} - Carrera: {estudiante['carrera']}")
        cursos=estudiante.get("cursos",{})
        if cursos:
            for curso, notas in cursos.items():
                promedio=(notas['tarea']+notas['parcial']+notas['proyecto'])/3
                print(f"Curso: {cursos}")
                print(f"Notas de tarea: {notas['tarea']}")
                print(f"Notas de parcial: {notas['parcial']}")
                print(f"Notas de proyecto: {notas['proyecto']}")
                print(f"Promedio: {promedio}")
        else:
            print("No tiene cursos registrados ")
    else:
        print("No hay estudiantes registrados ")






def menu():
    while true:
        print("\n ___ Menu ___")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estuiantes y cursos")
        print("3. Buscar estuiante por carnet")
        print("4. Salir")