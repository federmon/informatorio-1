'''4_
Escribir un programa que almacene una cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. Cuente el número de intentos
realizados por el usuario e imprimalo luego de la bienvenida al ingresar correctamente'''


clave_guardada = 'sala6'
clave_ingresada= input('ingrese su clave ')
contador = 1


while clave_guardada != clave_ingresada :
	clave_ingresada= input('Clave erronea, intente de nuevo: ')
	contador+=1
 
 
print("Felicidades! Te llevó ", contador, " intentos")




'''5_
Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes.
Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras,
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule
el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño,
más el número de ingredientes. En particular el costo total se calcula sumando:
- un costo fijo de preparación.
- un costo variable que es proporcional al tamaño de la pizza.
- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada
ingrediente extra tiene el mismo costo).


costo_fijo = 500
costo_peque = 1000
costo_mediana= 2000
costo_grandes = 3000
costo_ingrediente = 300

tamanio_pizza= int (input('ingrese el tamaño de la pizza y las opc son: 1_pequeña 2_mediana 3_grandes '))
cantidad_ingredientes= int (input('Ingrese la cantidad de ingredientes que quiere agregar a la pizza: '))


costo_final= costo_fijo + cantidad_ingredientes * costo_ingrediente

if tamanio_pizza ==1 :
	costo_final+=1000
elif tamanio_pizza == 2:
	costo_final+=2000
elif tamanio_pizza ==3:
  costo_final+=3000
  
precio_venta= costo_final*1.5

print("El precio de venta de su pizza elegida es de: ", precio_venta)
'''




 
