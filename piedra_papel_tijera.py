import random
p_p_t = ["Piedra", "Papel", "Tijera"]
puntaje_user = 0
puntaje_compu = 0

def compu_w():
    print("La computadora gana!")
def user_w():
    print("Tú ganas!")
def tie():
    print("Ha habido un empate parcial")



def jugar():
    #Entrada del usuario y elección de la computadora
    elec_usuario = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
    elec_usuario = elec_usuario.title()
    compu = random.choice(p_p_t)
    #Usar puntajes globales
    global puntaje_user
    global puntaje_compu

    #Validar entrada del ususario
    while elec_usuario not in p_p_t:
        elec_usuario = input("Ingresa \"Piedra\", \"Papel\" o \"Tijera\": ")
        elec_usuario = elec_usuario.title()
        print( "Entrada no válida, elige Piedra, Papel o Tijera")
        if elec_usuario in p_p_t:
            break
    #Imprimir elección de usuario y computadora
    print(f"La computadora elegió: {compu}")
    print(f"Tú elejiste: {elec_usuario}")
    #Compara las elecciones y da el veredicto
    if compu == "Tijera" and elec_usuario == "Piedra" or compu == "Piedra" and elec_usuario == "Papel" or compu == "Papel" and elec_usuario == "Tijera":
        user_w()
        puntaje_user +=1
    if compu == "Tijera" and elec_usuario == "Papel" or compu == "Piedra" and elec_usuario == "Tijera" or compu == "Papel" and elec_usuario == "Piedra":
        compu_w()
        puntaje_compu +=1
    if compu == elec_usuario:
        tie()
    print (f"Puntaje:\nTú = {puntaje_user} \nComputadora = {puntaje_compu}")

while True:#Bucle principal para repetir rondas del juego
    jugar()
    jugar_de_nuevo = input("Jugar otra ronda?: ")
    jugar_den_nuevo = jugar_de_nuevo.lower()
    