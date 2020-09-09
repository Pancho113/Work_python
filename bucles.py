# def run():
# contador = 0
# print(" 2 elevado a" + str(contador)+ "es igual a: "+ str(2**contador))

# contador = 1
# print(" 2 elevado a" + str(contador)+ "es igual a: "+ str(2**contador))


# if __name__ == "__main__":
#     run()

def run():
    LIMITE = 1000000

    contador = 0
    pontecia_2 = 2**contador
    while pontecia_2 < LIMITE:
        print(" 2 elevado a " + str(contador)+ " es igual a: "+ str(2**contador))
        contador = contador + 1
        pontecia_2 = 2**contador


if __name__ == "__main__":
     run()