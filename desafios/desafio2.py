texto = input("Ingresa un texto: ")
letra1 = input("Ingresa la primera letra: ")
letra2 = input("Ingresa la segunda letra: ")
letra3 = input("Ingresa la tercera letra: ")

# 1. Cantidad de veces que aparece cada letra
cant_letra1 = texto.count(letra1)
cant_letra2 = texto.count(letra2)
cant_letra3 = texto.count(letra3)
print(f"La letra {letra1} aparece {cant_letra1} veces")
print(f"La letra {letra2} aparece {cant_letra2} veces")
print(f"La letra {letra3} aparece {cant_letra3} veces")

# 2. Cantidad de palabras en el texto
palabras = texto.split()
cant_palabras = len(palabras)
print(f"Hay {cant_palabras} palabras en el texto")

# 3. Primera y última letra
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra es {primera_letra} y la última letra es {ultima_letra}")

# 4. Texto en orden inverso
texto_inverso = texto[::-1]
print("El texto en orden inverso es:", texto_inverso)

# 5. Si la palabra "python" aparece en el texto
if "python" in texto.lower():
    print("La palabra 'python' aparece en el texto")
else:
    print("La palabra 'python' no aparece en el texto")