import random

    

def run():
    vida = int(input("Ingrese tus vidas: "))

    numero_aleatorio = random.randint(1, 100)
    
    while True:
        
        if vida == 0 :
            print("HAS PERDIDO CONTRA EL PC!!!!")
            break
        numero_elegido = int(input("Elige un número del 1 al 100: "))
        if numero_elegido < numero_aleatorio:
            print("Busca un número más Grande")
            
            vida -=1
        elif numero_elegido == numero_aleatorio:
            print("HAS GANADO EL JUEGO INCREIBLE!!!!!")
            break
        else:
            print("busca un número mas pequeño")
            
            vida -=1
    


if __name__ == "__main__":
    run()