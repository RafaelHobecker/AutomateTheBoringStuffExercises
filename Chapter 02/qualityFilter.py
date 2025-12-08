# Imagina que tienes una lista de tiempos de respuesta de un servidor
# (en milisegundos). Tu jefe quiere saber cuántos de estos tiempos son
# "Lentos"(mayores a 80 ms).

tiempos = [45,120,30,95,88,50,200,75]

contador = 0

for tiempo in tiempos:
    if tiempo>80:
        contador += 1
        print(f"El tiempo de {tiempo} ms es lento.")

print(f"La cantidad total de tiempos lentos es de {contador}.")

