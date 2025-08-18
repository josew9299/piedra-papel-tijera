import random
p_p_t = ["Piedra", "Papel", "Tijera"]


vict_user = 0
vict_compu = 0

def puntaje():
    print(f"Tú llevas ,{vict_user}, puntos")
    print(f"La computadora lleva ,{vict_compu}, puntos")
def compu_w():
    print("La computadora gana!")
def user_w():
    print("Tú ganas!")
def tie():
    print("Ha habido un empate parcial")

def jugar(compu,user):

    user = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
    user = user.title()
    compu = random.choice(p_p_t)

    try:
        while user not in p_p_t:
            user = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
            user = user.title()
            if user.title() not in ppt:
                user = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
            user = user.title()
            print( "Entrada no válida, elige Piedra, Papel o Tijera")
            
            



        if compu == "Tijera" and user == "Pierda":
            user_w()
        if compu == "Tijera" and user == "Papel":
            compu_w()
        if compu == "Piedra" and user == "Tijera":
            compu_w()
        if compu == "Piedra" and user == "Papel":
            user_w()
        if compu == "Papel" and user == "Tijera":
            user_w()
        if compu == "Papel" and user == "Piedra":
            compu_w()
        if compu == "Piedra" and user == "Piedra":
            tie()
        if compu == "Tijera" and user == "Tijera":
            tie()
        if compu == "Papel" and user == "Papel":
            tie()
            return
    except TypeError:
        return "Error"

print(compu)
print(user)




jugar(compu, user)

if jugar(compu_w,user_w):
    vict_compu +=1
if jugar(user_w,user_w):
    vict_user +=1
else:
    print("")

print("")
print("")