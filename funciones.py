#Funciones 
#def name_funtion(params):
#   code

# Sin parametros y sin retorno
def saluda():
    print("Hola a todos")

saluda()

# Con parametros, sin retorno 
def duplica(num):
    print(num * 2)

duplica(5)

def suma(num1, num2):
    print(f"La suma de los numeros es:  {num1 + num2}")

suma(23, 45)

#Parametros opcionales, sin retorno 
def get_lista(al1 ="Jose, al2 ="Darlen"):
    return [al1, al2]

    my_list = get_lista()
    print(my_list)
    my_list = get_lista("Peter")
    print(my_list)
    my_list = get_lista("Peter Parker", "Tony Stark")
    print(my_list)
    my_list = get_lista(al2="Peter Parker", al1="Tony Stark")
    print(my_list)
    