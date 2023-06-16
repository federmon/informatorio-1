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

inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
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
    editar = 0
    while editar<0 and editar>len(inmuebles):
      editar = input('Que inmueble desea editar? ingrese el numero correspondiente ')
      if editar.isdigit():
        editar=int(editar)
    parametro = 0
    while parametro<= 0 or parametro > 7:
      parametro = input(f'{inmuebles[editar-1]} \nQue parametro desea modificar? \n1_año 2_metros 3_habitaciones 4_garaje 5_zona 6_estado \nIngrese su nro: ')
      if parametro.isdigit():
        parametro=int(parametro)
    nuevoValor = ''
        
    if parametro == 1:
      parametro='año'
      while not nuevoValor.isdigit():
        nuevoValor = input('Ingrese el año mayor o igual a 2000 que desea guardar (un número entero: ')
        if nuevoValor.isdigit():
          if int(nuevoValor)>=2000:
            nuevoValor=nuevoValor
          else:
            nuevoValor=''
      nuevoValor=int(nuevoValor)
      
            
        
    elif parametro == 2:
      parametro='metros'
      while not nuevoValor.isdigit():
        nuevoValor = input('Ingrese los metros cuadrados mayor a 60: ')
        if nuevoValor.isdigit():
          if int(nuevoValor)>=60:
            nuevoValor=int(nuevoValor)
                
    elif parametro == 3:
      parametro='habitaciones'
      while not nuevoValor.isdigit():
        nuevoValor = input('Ingrese la cantidad de habitaciones (minimo 2): ')
        if nuevoValor.isdigit():
          if int(nuevoValor)>=2:
            nuevoValor=int(nuevoValor)
  
    elif parametro == 4:
      parametro='garaje'
      while nuevoValor != 'S' or nuevoValor != 's' or nuevoValor != 'n' or nuevoValor != 'N':
        nuevoValor = input('Ingrese "S" si tiene garaje o ingrese "N" si no tiene garaje \nIngrese su respuesta:')
      if nuevoValor == 'S' or nuevoValor == 's':
        nuevoValor = True
      elif nuevoValor == 'n' or nuevoValor == 'N':
        nuevoValor = False
            
    elif parametro == 5:
      parametro='zona'
      while nuevoValor != 'A' or nuevoValor != 'B' or nuevoValor != 'C':
          nuevoValor = input('Ingrese la zona segun corresponda A B C en mayuscula \nIngrese su respuesta:')
            
    elif parametro == 6:
      parametro='estado'
      while nuevoValor != 'D' or nuevoValor != 'd' or nuevoValor != 'V' or nuevoValor != 'v' or nuevoValor != 'R' or nuevoValor != 'r':
          nuevoValor = input('Ingrese "D" si está Disponible, "V" si está Vendido o "R" si está reservado \nIngrese su respuesta:')
      if nuevoValor == 'D' or nuevoValor == 'd':
          nuevoValor = 'Disponible'
      elif nuevoValor == 'V' or nuevoValor == 'v':
          nuevoValor = 'Vendido'
      elif nuevoValor == 'R' or nuevoValor == 'r':
          nuevoValor = 'Reservado'

      

    inmuebles[editar-1][parametro]=nuevoValor
    print(f'{inmuebles[editar-1]} \nLa modificacion se ha realizado con exito')
    
#opciones para el usuario    
opcion = int(input('1) Agregar inmueble \n2) Eliminar inmueble\n3)Editar inmueble \nIngrese su respuesta: '))
if opcion == 1:
    inmueble = input('ingrese nuevo inmueble')
    agregar_inmueble(inmueble)
    print(inmuebles)
elif opcion == 2:
    i=1
    for inmueble in inmuebles:
        print(f'{i}) {inmueble}')
        i+=1
    eliminar=int(input('Que inmueble desea eliminar? ingrese el numero correspondiente: '))
    eliminar_inmueble(inmuebles[eliminar-1])  
    i=1
    for inmueble in inmuebles:
        print(f'{i}) {inmueble}')
        i+=1
    print('inmueble eliminado')
elif opcion==3:
    i=1
    for inmueble in inmuebles:
        print(f'{i}) {inmueble}')
        i+=1
    editar_inmueble(inmuebles)    
   


#La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
#los inmuebles cuyo precio sea menor o igual que el dado y el estado sea Disponible o
#Reservado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada
#diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
#reglas de precio en función de la zona.

'''   
def busqueda(inmuebles,preciomax):
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
                resultado_de_la_busqueda.append(inmueble)    
            
  return resultado_de_la_busqueda       


print(busqueda(inmuebles,15000)) 
'''