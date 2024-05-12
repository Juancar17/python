import random

# Lista de palabras para el juego
palabras = ["pepino", "azul", "mandarina", "completo", "jugar"]

# Seleccionar una palabra al azar de la lista
palabra_secreta = random.choice(palabras)

print("BIENVENIDO AL JUEGO DEL AHORCADO")
print("Intenta adivinar la palabra seleccionada...")

# Inicializar la palabra oculta con guiones bajos del mismo tamaño que la palabra secreta
palabra_oculta = "_" * len(palabra_secreta)

# Función para adivinar letras de la palabra
def jugar_ahorcado():
    global palabra_oculta  # Declarar palabra_oculta como global
    
    vidas = 10  # Número de vidas inicial
    
    while vidas > 0:
        letra_introducida = input("Introduce una letra: ").lower()  # Pedir al usuario una letra
        
        if len(letra_introducida) != 1 or not letra_introducida.isalpha():
            print("Por favor, introduce una sola letra válida.")
            continue
        
        if letra_introducida in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
            # Actualizar la palabra oculta con la letra adivinada
            nueva_palabra_oculta = ""
            for letra_real, letra_oculta in zip(palabra_secreta, palabra_oculta):
                if letra_real == letra_introducida:
                    nueva_palabra_oculta += letra_real
                else:
                    nueva_palabra_oculta += letra_oculta
            palabra_oculta = nueva_palabra_oculta  # Actualizar palabra_oculta globalmente
            print("Palabra:", palabra_oculta)
            
            if palabra_oculta == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                break
        else:
            print("La letra no está en la palabra.")
            vidas -= 1
            print("Te quedan", vidas, "vidas.")
    
    if vidas == 0:
        print("¡Oh no! Te has quedado sin vidas. La palabra era:", palabra_secreta)

# Llamar a la función para jugar el juego del ahorcado
jugar_ahorcado()
