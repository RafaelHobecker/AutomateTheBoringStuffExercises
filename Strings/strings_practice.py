#1. Definicion y Comillas

# Definicion con comillas dobles
nombre_curso = 'Programacion en Python'

#Definicion con comllas simples
nombre_alumno = 'Aldo'

#Esto es util si el texto contiene una comilla simple ( apostrofe)
descripcion = "Esto es un ejemplo de 'Strings' de texto."
print(descripcion)

#2. Concatenacion (Unir Strings)
# Puedes unir dos o mas Strings usando el operador +.

saludo = "Hola"
lenguaje = "Python"
mensaje_completo = saludo + lenguaje
print(mensaje_completo)


#3. F-Strings (Formato Avanzado)
# Forma mas moderna y recomendada de construir mensajes complejos.
# Permite insertar variables directamente dentro de un String anteponiendo la letra f a las comillas.

edad = 31
mensaje_f = f"El alumno {nombre_alumno} tiene {edad} anhos y esta aprendiendo {lenguaje}"
print(mensaje_f)

#4. Daily Challenge

#a. Crea una variable nombre con tu nombre completo.
nombre = "Aldo Rafael Estigarribia Hobecker"

#b. Crea una variable libro con el titulo del libro que estas usando
libro = "Automate the Boring Stuff"

#c. Crea una variable chapter con el numero 2
chapter = 2

#d. Crea un F-String que diga: "Hola, [Tu nombre completo]. Estas estudiando el Chapter 2 de [Titulo del Libro].
enunciado = f"Hola, {nombre}. Estas estudiando el Chapter {chapter} del libro {libro}."
print(enunciado)
#fin


#5. .title() (Titulo)
# Convierte la primera letra de cada palabra a mayuscula, dejando el resto en minuscula.

nombre_artistico = "elvis aaron presley"
nombre_formato_titulo = nombre_artistico.title()
print(nombre_formato_titulo)
#Salida: Elvis Aaron Presley

#7. upper() (MAYUSCULAS)
#Convierte todo el String a mayusculas.

nombre_minuscula = "09xcgih3w"
nombre_mayuscula = nombre_minuscula.upper()
print(nombre_mayuscula)
#Salida: 09XCGIH3W


#8. .lower() (minusculas)
#Convierte todo el String a minusculas.

marca = "aPpLe"
marca_minuscula = marca.lower()
print(marca_minuscula)
#Salida: apple

#9. Daily Challenge 2
#Crea una variable llamada usuario_input y asignale un valor que mezcle mayusculas y minusculas
usuario_input = 'AlDo RaFaEl'

#Crea una segunda variable llamada noombre_normalizado que tome usuario_input y le aplique el metodo .lower()
nombre_normalizado = usuario_input.title()

#Crea una tercera variable llamada nombre_url que tome usuario_input y le aplique el metodo .lower()
nombre_url = usuario_input.lower()

#Imprimir el nombre normal
print(nombre_normalizado)

#Imprimir el nombre en minusculas
print(nombre_url)


#10. Problema de inclusion de espacios innecesarios al inicio o al final del texto.

#.rstrip() Elimina espacios a la derecha(trailling spaces).
auxiliar = "Python "
auxiliar_corregido = auxiliar.rstrip()

#Esto imprime "Python" en vez de "Python "
print(auxiliar_corregido)


#.lstrip() Elimina espacios a la izquierda (leading spaces).
left = " Java"
left_corregido = left.lstrip()

#Esto imprime "Java" en vez de " Java"
print(left_corregido)

#.strip() Elimina espacios de ambos lados (izquierda y derecha).
both = " C++ "
both_corregido = both.strip()

#Esto imprime "C++" en vez de " C++ ".
print(both_corregido)

#11. Daily Challnge 3

# Vamos a simular la entrada de un usuario descuidado:

#Crea una variable usuario_mal_escrito y asignale el valor: " \t \n aldo_rafael \n \t "
usuario_mal_escrito = " \t \n aldo_rafael \n \t "

#Crea una variable usuario_limpio que tome el valor de la variable anterior y le aplique el metodo .strip()
usuario_limpio = usuario_mal_escrito.strip()

#Imprimir usuario_mal_escrito
print(usuario_mal_escrito)

#Imprimir usuario_limpio
print(usuario_limpio)






