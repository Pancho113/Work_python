import random

def run ():
    print("""
    El juego consiste en escribir un numero mayor al que genera el sistema en un rango del 1 al 10,
    tienes hasta 3 oportunidades de fallar al inicio.
    El sistema genera un numero aleatoria en cada intento!
    Suerte!""") 

    vidas = 3 
    numero_sistema = random.randrange(11)
    # print(numero_sistema) #Imprime el numero de sistema 
    while vidas > 0: 
        numero_usuario = int(input('Cual es tu numero?: '))
        if numero_usuario < numero_sistema:
            vidas -= 1
            print('Fallaste! Pierdes una vida. Intenta de nuevo')
            print(f'Te quedan {vidas} vidas')

        elif numero_usuario == numero_sistema:
            vidas -= 1
            print('Fallaste! Pierdes una vida. Intenta de nuevo')
            print(f'Te quedan {vidas} vidas')

        elif numero_usuario < 0 or numero_usuario>10:
            vidas -= 1
            print('Numero fuera del rango! Pierdes una vida')
            print(f'Te quedan {vidas} vidas')

        else:
            print('Ganaste!! Congrats')
            exit()
    print('Se te acabaron las vidas')
    
if __name__ == "__main__":
    run()