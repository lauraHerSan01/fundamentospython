students = []

def show_students():
    for student in students:
        print("Alumno ->", Student)

def add_student(student):
    students.append(student)


def remove_student(student):
    try:
        student.remove(student)
    except Exceotion:
        print("No existe ")

choice_text = '''
Elige una opcion: 
    1- Insertar 
    2- Mostrar
    3- Salir 
'''

while   True:
    choice = int ( input (choice_text))
    if choice == 1:
        student = input("Ingresa student: ")
        add_student (student)
    elif choice == 2:
        show_students()
    elif choice == 3:
        student = input("Ingresar student a eliminar: ")
        remove_student (student )
    elif choice == 4:
        break 
    else:
        print('Incorrect Option')