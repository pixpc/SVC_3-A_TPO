# Practica 2 - Listas y Cadenas
def main():

    #Pedir una frase 
    texto = input("Ingresa una frase:")

    #Convertir la frase en split
    palabras = texto.split()
    print("\nLista generada:", palabras)

    #Mostrar las palabras en mayusculas 
    print("\nPalabras en mayusculas :")
    [print(p.upper()) for p in palabras]

    #Contar ocurrencias de cada palabra
    buscar = input("\nIngrese una palabra a buscar en la lista:")
    veces = palabras.count(buscar)
    print(f"La palabra '{buscar}' aparece {veces} veces en la lista.")

    #Reemplazar palabra
    OG = input("\nPalabra a sustituir:")
    nueva= input("Nueva palabra:")
    resultado = texto.replace(OG, nueva)
    print("\nFrase final:", resultado)

if __name__ == "__main__":
    main()