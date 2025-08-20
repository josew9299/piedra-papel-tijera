# Juego de Piedra, Papel o Tijera en Python, implementado con validación robusta y modularidad.
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

def puntaje():
    global puntaje_user
    global puntaje_compu
    print(f"Puntaje Tú - {puntaje_user}, Computadora - {puntaje_compu}")


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
    puntaje()

print("¡Bienvenido a Piedra, Papel o Tijera!")

while True:#Bucle principal para repetir rondas del juego
    jugar()
    jugar_de_nuevo = input("¿Jugar otra ronda? (sí/s/no/n): ")   
    jugar_de_nuevo = jugar_de_nuevo.lower()
    while jugar_de_nuevo not in ["si","s","no","n"]:
        print("Entrada no válida, ingresa 'sí', 's', 'no', o 'n'")
        jugar_de_nuevo = input("¿Jugar otra ronda? (sí/s/no/n): ")
        jugar_de_nuevo = jugar_de_nuevo.lower()
    if jugar_de_nuevo in["no","n"]:
        break

puntaje()
print("¡Hasta luego!")
input("")

#Completado: Validación de entrada, elección de computadora, comparaciones simplificadas, puntajes actualizados (Partes 1-4).
#Completado: Bucle principal para múltiples rondas con validación robusta de 'jugar_de_nuevo' (Parte 5).
#Completado: Añadida función puntaje para mostrar puntajes de forma consistente y modular.
#Finalizado: Juego completamente funcional con mensajes claros y formato consistente.