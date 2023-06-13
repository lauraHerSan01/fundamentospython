import  random

int_rand = random.ranint(0,2)

if int_rand == 0:
    choice_maq = "piedra"
elif int_rand ==1:
    choice_maq = "papel"
else:
    choice_maq = "Tijeras"

    print(choice_maq)

#Elige usuario 
choice_txt = '''
Escribe una aoperacion"
piedra 
papel 
tijeras 
'''

choice_user = imput(choice_maq)

print("Maquina ->", choice_maq)
print("Usuario ->", choice_user)

if choice_maq == choice_user:
    print("Es un empaque")
else:
    if choice_maq == "Piedra" and choice_user == "Papel":
        print("Gana Usuario!")
    elif choice_maq == "Piedra " and choice_user == "Tijera":
        print("Gana Maquina")
    elif choice_maq == "Papel" and choice_user == "Tijera":
        print("Gana Usuario!")
    elif choice_maq == "Papel " and choice_user == "Piedra":
        print("Gana Maquina")
    elif choice_maq == "Tijera" and choice_user == "Piedra":
        print("Gana Usuario!")
    elif choice_maq == "Tijera " and choice_user == "Papel":
        print("Gana Maquina")