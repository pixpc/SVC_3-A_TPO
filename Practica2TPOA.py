# Practica 2 - Listas y Cadenas

frase = input("Ingresa una frase: ")

lista_palabras = frase.split()
print("\nLista de palabras:", lista_palabras)

print("\nPalabras en mayúsculas:")
for palabra in lista_palabras:
    print(palabra.upper())

palabra_buscar = input("\n¿Qué palabra quieres contar en la frase?: ")
conteo = frase.split().count(palabra_buscar)
print(f"La palabra '{palabra_buscar}' aparece {conteo} veces.")

palabra_reemplazar = input("\n¿Qué palabra quieres reemplazar?: ")
nueva_palabra = input("¿Por cuál palabra la quieres reemplazar?: ")
frase_modificada = frase.replace(palabra_reemplazar, nueva_palabra)
print("\nFrase modificada:", frase_modificada)