# podemos declarar variables y las podemos unir
mensaje = "hola"

# con el operador += podemos unir las variables 
mensaje += "  "
mensaje += "Jean"

# nuevamente imprimimos 
print(mensaje)

# ____________________________________________

# Ejemplo con cocatenacion 
print("Concatenacion")

mensaje = "hola"
espacio = "  "
nombre = "Jean"

# en este caso usamos el + para concatenar 
print(mensaje + espacio + nombre)



# __________________________________________

print("Esto es una suma")

# declaramos variables de numeros 
number1 = 4
number2 = 7

# Hacemos la operacion 
result= number1 + number2

# Usamos str para sustituir un valor numerico a un valor tipo texto 
result= str(result)

print("El resultado es : " + result)


# __________________________________________

print("Busqueda")

# en el caso de buscar 
mensaje = "hola Jean"

# declaramos una variable que tome otra pero con el metodo find y la cadena a buscar 
buscar_subcadena = mensaje.find('Jean')

# imprimimos y nos arroja la posicion basandonos que 0 equivale a la primer posicion 
print(buscar_subcadena)


# __________________________________________

print("comparacion")

# en el caso de comparar 
mensaje_1 = "hola"
mensaje_2 = "hola"

# solo tenemos que usar el doble igual (==) cuando queremos saber si un dato es igual al de otra variable indicada 
print(mensaje_1 == mensaje_2)