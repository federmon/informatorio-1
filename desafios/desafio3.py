'''Vamos a crear un juego completamente funcional.
Para ello el programa debe:
 Pedir al usuario que ingrese su nombre.
 Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
 Generar aleatoriamente un número entero entre 1 y 100.
tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
 Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
El "número" ingresado por el usuario puede:
 No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
tip 2: con el método isdigit() puedes saber si es posible convertir a entero
 Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
 Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
 Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
lo adivinó.
 Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
debes descontarle un intento.
 En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
ingrese otro número.
 Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
número que tenía que adivinar.'''

# Le solicita al usuario que ingrese su nombre y le explica brevemente las reglas del juego.
nombre = input('¡Hola! ¿Cuál es tu nombre? ')
numero = input(f'¡Genial {nombre}¡ Tenés que adivinar el número entero del 1 al 100 que estoy pensando \n Sólo tenés 8 intentos. \n-->   ' )

# Importa el modulo random y genera aleatoriamente un número entero entre 1 y 100.
import random
aleatorio = random.randint(1, 100)

# Creo la constante para inicializar en 8 el contador de número de intentos restantes.
intentos = 8

# Comienza el ciclo de adivinanza según cada alternativa.
while intentos > 1:

    # Verifica si el número ingresado es un entero.    
    if numero.isdigit():
        numero = int(numero)
        
        # Con la condicional múltiple verifica si el número ingresado es menor, mayor o igual al número a adivinar.
        if numero < aleatorio:
            intentos = intentos - 1
            print(f'El numero a adivinar es mayor \n te quedan {intentos} intentos')
            numero = input('ingresa otro numero \n-->  ')
    
        elif numero > aleatorio:
            intentos = intentos - 1
            print(f'El numero a adivinar es menor \n te quedan {intentos} intentos')
            numero = input('ingresa otro numero \n-->  ')
        else:
            break
    else:
        print(f'       ¡ERROR! \n {numero} no es un numero entero.')
       ### German. Le agregue las 2 linea que siguen, era lo unico que le faltaba que le faltaba. ##BORRAR
       ###No debe descontar intentos en esta línea en las consignas está que: " Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si debes descontarle un intento."
        print(f'Aún te quedan {intentos} intentos')
        numero = input('Ingresa otro número. \n-->  ')

               
# Verifica si el usuario se quedó sin intentos, le informa de ello y el número que tenía que adivinar
if int(numero) == aleatorio:
	print(f'     ¡¡¡ADIVINASTE!!! Felicitaciones {nombre} \nLo hiciste en el intento número {9-intentos}')
else:
  print(f'       ¡PERDISTE! \nNo te quedan más intentos \nEra el número {aleatorio}.\n Seguí participando.')