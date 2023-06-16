"""
Definir una función que calcule la longitud de una lista
o una cadena dada. No tenemos que usar el método len()
"""

"""
def longitud (elemento):
	contador = 0
	for i in elemento:
		contador +=1
  
	print(f'La longitud es {contador}')
   
cadena=	input('Ingresar una cadena o string y le devolveremos su longitud!: ')

lista_cargada=['mateo','info',2023]
cadena_vacia= ''
lista_vacia=[]
longitud(lista_vacia)
"""









"""
Definir una función max_de_tres(), que tome tres números
como argumentos y devuelva el mayor de ellos. Sin math.max() y ningún método.
"""


def max_de_tres(nro1,nro2,nro3):
  if nro1 > nro2 and nro1 > nro3:
    return nro1
  elif nro2 > nro3:
    return nro2
  else:
    return nro3

resultado=max_de_tres(7,7,3)
print(f'El número:{resultado} es el mayor')






"""
Escribir una función suma() y una función multiplicacion() que sumen y
multipliquen respectivamente todos los números de una lista.
"""


"""
Definir una función que calcule la longitud de una lista
o una cadena dada. No tenemos que usar el método len()
"""