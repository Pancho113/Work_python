def conversor(tipo_pesos, Valor_dolar):
    pesos = input("¿Cuantos pesos"+ tipo_pesos +" tienes? ")
    pesos = float(pesos)
    dolares = pesos / Valor_dolar
    dolares = round(dolares, 2)#Tomamos el contenido que le ponemos dos decimales
    dolares = str(dolares)
    print("tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion  = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Eliga una opción correcta porfavor!!")




