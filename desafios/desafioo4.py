'''
Desafío 4: La inmobiliaria
Requisitos técnicos:
- Operadores.
- Estructuras de datos.
- Estructuras de control de flujo.
- Funciones
Una inmobiliaria de tu ciudad solicita un sistema para automatizar la gestión de sus inmuebles.
Se te pide construir un programa que permita:
 Agregar, editar y eliminar inmuebles a la lista.
Las funciones deben ajustarse al formato de lista y reglas de validación.
 Cambiar el estado de un inmueble, sin modificar sus demás datos.
Las funciones deben ajustarse al formato de lista y reglas de validación.
 Hacer búsqueda de inmuebles en función de un presupuesto dado.
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
reglas de precio en función de la zona.
Formato de lista
[{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
Reglas de validación
 Inmuebles solo de zona: A, B o C.
 Inmuebles con estado: Disponible, Reservado o Vendido.
 No opera con inmuebles:
 Anteriores al año 2000.
 Menores de 60 metros cuadrados.
 Menores de 2 habitaciones.
Reglas de precio
 Zona A: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100)
 Zona B: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 1.5
 Zona C: precio = (metros x 100 + habitaciones x 500 + garaje x 1500) x (1 - antigüedad / 100) x 2
'''


inmuebles = [
{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
{'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
{'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
{'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
{'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]
 

#Agregar, editar y eliminar inmuebles a la lista.

def agregar_inmueble(inmueble):
    inmuebles.append(inmueble)
    return inmuebles

def eliminar_inmueble(inmueble):
    inmuebles.remove(inmueble)
    return inmuebles

def editar_inmueble(inmuebles):
    editar=int(input('Que inmueble desea editar? ingrese el numero correspondiente'))
    parametro=(input(f'{inmuebles[editar-1]} \nQue parametro desea modificar?'))
    parametro = 'año'
    nuevoValor=input('ingrese el nuevo valor')
    inmuebles[editar-1][parametro]=nuevoValor
    print(f'{inmuebles[editar-1]} \nLa modificacion se ah realizado con exito')

#La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
#los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
#Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
#diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
#reglas de precio en función de la zona.

'''def busqueda(inmuebles,preciomax):
    resultado_de_la_busqueda = []    
    for inmueble in inmuebles:
        if inmueble["estado"]=='Disponible' or inmueble["estado"]=='Reservado':
            if inmueble["zona"]=='A':
                precio = (inmueble["metros"]*100 + inmueble["habitaciones"]* 500 + inmueble["garaje"]*1500) * (1 - ((2023-inmueble["año"]) / 100))
            elif inmueble["zona"]=='B':
                precio = 1.5*(inmueble["metros"]*100 + inmueble["habitaciones"]* 500 + inmueble["garaje"]*1500) * (1 - ((2023-inmueble["año"]) / 100))
            elif inmueble["zona"]=='C':
                precio = 2*(inmueble["metros"]*100 + inmueble["habitaciones"]* 500 + inmueble["garaje"]*1500) * (1 - ((2023-inmueble["año"]) / 100))
            
            if precio <= preciomax:
                inmueble["precio"] = precio
                resultado_de_la_busqueda.append(inmueble)    
            
    return resultado_de_la_busqueda 
'''
bandera= True
while bandera :   

  opcion = int(input('1) Agregar inmueble \n2) Eliminar inmueble\n 3)Editar inmueble\n4)Buscar \n5)Salir'))

  if opcion == 1:
      inmueble = []
      inmueble["año"] = (input('ingrese el año del inmueble'))
      inmueble["metros"] = input('ingrese los metros del inmueble')
      inmueble["habitaciones"] = input('ingrese la cantidad de habitaciones del inmueble')
      inmueble['garaje'] = input('el inmueble tiene garaje? S/N')
      if inmueble['garaje'].lower == s:
        inmueble['garaje'] = True
      else:
          inmueble['garaje'] = False
      
      inmueble['zona'] = input('ingrese la zona del inmueble\nA\nB\nC')
      while inmueble['zona'].lower!='a' and inmueble['zona'].lower!='b' and inmueble['zona'].lower!='c':
        print('ERROR.\n La opcion ingresada no es correcta')
        inmueble['zona'] = input('ingrese la zona del inmueble\nA\nB\nC')
      
      inmueble['estado'] = input('ingrese el estado del inmueble: Disponible, Reservado o Vendido')

      agregar_inmueble(inmueble)
      print(inmuebles)
