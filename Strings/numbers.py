# Ejemplos de Tipos de Datos Numericos

#1. Integers (Enteros)
# Se usan para contar cosas que no tienen decimales(como el numero de personas o el numero de veces que se ejecuta un bucle).

dias_mes = 30 #Esto es un 'int'
usuarios_activos = 4500
print("La variable dias_mes es de tipo: ",type(dias_mes))
# Salida: <class 'int'>


#2. Floats (Punto Flotante/Decimal)
#Se usan para cantidades que requieren precision ( como dinero, temperatura o porcentajes).

temperatura = 25.5
PI = 3.14159
print("La variable temperatura es de tipo: ",type(temperatura))
print("La variable PI es de tipo: ",type(PI))

#3. Ejemplos de Operaciones Aritmeticas.

# Variables para el ejemplo.
precio_unidad = 1.05
cantidad_a_comprar = 10

# Multiplicacion (el resultado de multiplicar un float por un int es siempre un float).
costo_parcial = precio_unidad * cantidad_a_comprar
print(f"Costo Parcial: {costo_parcial}")

# Operacion de Division (el resultado de la division es siempre un float, incluso si es exacto.

resultado_division = 10 / 2
print(f"Resultado de 10 / 2: {resultado_division}")
print("El Resultado es de tipo: ",type(resultado_division))


# Operacion de Exponente (cuadrado)

area_cuadrado = 5 ** 2
print(f"Area: {area_cuadrado}")
#Salida: Area 25


#4. Daily Challenge

#Crear una variable precio_bitcoin con un valor float (ej: 65432.78)
precios_bitcoin = 65432.78

#Crear una variable cantidad_comprada con un valor float (ej: 0.5)
cantidad_comprada = 0.5

#Crear una variable costo_total multiplicando (*) las dos anteriores
costo_total = precios_bitcoin * cantidad_comprada

print(f"Costo Total: {costo_total}")
print(type(costo_total))



#5. Daily Challenge

#Usa la variable costo_total que acabas de calcular

#Crea una variable mensaje_final que use concatenacion(+) para unir el texto:
# "El costo final de la compra fue de:" + costo_total + "USD"

#   (Necesitamos usar str() para convertir costo_total antes de concatenarlo).

print("El costo final de la compra fue de: " + str(costo_total) + " USD.")