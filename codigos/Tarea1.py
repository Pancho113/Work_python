import time

def enumeracion(respuesta, objetivo):
    start = time.time()

    while respuesta**2 < objetivo:
        respuesta += 1

    end = time.time()
    if respuesta**2 == objetivo:
        print(f' La raiz cuadrada de {objetivo} es  {respuesta}, tiempo es {end -start} segundos')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta, tiempo es {end -start} segundos')


def aproximacion(respuesta, objetivo, epsilon, paso):
    start = time.time()

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(abs(respuesta**2 - objetivo), respuesta)
        respuesta+= paso

    end = time.time()
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}, el tiempo fue {end - start} segundos')
    else:
        print(f'No se encontro la raiz cuadrada de {objetivo} es {respuesta}, el tiempo fue {end - start} segundos')



def busqueda_binaria(respuesta, objetivo, epsilon, bajo, alto, num):

    start = time.time()

    while abs(respuesta**2 - objetivo) >= epsilon:

        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2

        num += 1

    end = time.time()

    print(f'Para resolver hizo {num} iteraciones y se demoro {end - start} segundos')

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
    menu = """ 
    Hola soy el computador!!!

    Vamos a resolver el problema de encontrar la raiz cuadrada de un número.
    Por esto se pide por pantalla que método utilizar:
    1.- Enumeracion exautiva.
    2.- Aproximación.
    3.- Busqueda Binaria.

    ¿Ingrese que método ocupar (1, 2, 3)?"""

    eleccion = int(input(menu))

    objetivo  = int(input('Escoge un número: '))
    

    if eleccion == 1 :
        respuesta = 0 
        enumeracion(respuesta, objetivo)
    if eleccion == 2 :
        epsilon = 0.001
        paso = epsilon**2
        respuesta = 0.0
        aproximacion(respuesta, objetivo, epsilon, paso)
    if eleccion == 3 :
        epsilon = 0.000001
        bajo = 0.0
        alto = max(1.0, objetivo)
        respuesta = (alto + bajo)/2
        num = 0 #numero para contar iteraciones
        busqueda_binaria(respuesta, objetivo, epsilon, bajo, alto, num)


if __name__ == "__main__":
    run()