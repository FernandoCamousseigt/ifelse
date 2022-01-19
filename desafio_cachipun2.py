import random

#el sistema (player2) elige su nombre y se presenta

listado_nombres_player2 = ["El Profesor", "Moscu", "Tokio", "Denver", "Rio", "Helsinki", "Oslo", "Berlin", "Nairobi"]

nombre_player2 = random.choice(listado_nombres_player2)  #con random.choice elige 1 elemento de la lista al azar

print("Hola soy", nombre_player2)

#p2 pregunta nombre y saluda

nombre_jugador = input("Cual es tu nombre?") 

print("Hola", nombre_jugador)

#p2 pregunta opciones piedra papel o tijera

lista_opciones = ["piedra", "papel", "tijera"]

print("Las opciones son:", lista_opciones)

respuesta_jugador = input("ca- chi - pun! escoge tu opcion:").lower()

try: 
    print(nombre_jugador, "escoge:", respuesta_jugador)
except NameError:
    print("Tu respuesta es inválida: debe ser piedra, papel o tijera. Juega de nuevo")



#p2 genera un respuesta aleatoria: piedra, papel o tijera

numero_aleatorio = random.randint(0,2)

respuesta_sistema = lista_opciones[numero_aleatorio]
print(nombre_player2, "elige:" , respuesta_sistema)


#se comparan las respuestas  +  Indica el ganador

if respuesta_jugador == respuesta_sistema:
    print("Es empate")
elif respuesta_jugador == "piedra" and respuesta_sistema == "tijera":
    print("Gana:", nombre_jugador)
elif respuesta_jugador =="piedra" and respuesta_sistema == "papel":
    print("Gana:", nombre_player2)
elif respuesta_jugador =="papel" and respuesta_sistema == "tijera":
    print("Gana:", nombre_player2)
elif respuesta_jugador =="papel" and respuesta_sistema == "piedra":
    print("Gana:", nombre_jugador)
elif respuesta_jugador =="tijera" and respuesta_sistema == "piedra":
    print("Gana:", nombre_player2)
elif respuesta_jugador =="tijera" and respuesta_sistema == "papel":
    print("Gana:", nombre_jugador)
else:
    print("Tu respuesta es inválida: debe ser piedra, papel o tijera. Juega de nuevo")

input()

