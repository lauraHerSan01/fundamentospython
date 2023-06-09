# Funcion imput -> retorna string

name = input('como te llamas?\n')
age = int (input('Cuantos años tienes?\n'))
future = int (input('cuantos años mas?\n') )


print("Hola " + name)
print("En "  +str (future) + " años tendras " + str(age + future))


#Format String
#"""
# Hola Laura, en 3 años tendras 22 años
#"""

text_complete = "Hola {}, en {} años tendras {} años"
print(text_complete. format (name, age + future))  

print(f"Hola {name}, en {future} años tendras {age + future} años")