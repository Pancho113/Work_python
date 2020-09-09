def run():
    mi_diccionario = {
        "llave1" :  1,
        "llave2" : 2,
        "llave3" : 3,
    }

    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])

    Poblacion_paises ={
        "Argentina": 4493716,
        "Brasil": 21014125,
        "Colombia": 5032364,
    }

    # print(Poblacion_paises["Argentina"])

    # for pais in Poblacion_paises.keys():
    #     print(pais)
    # for pais in Poblacion_paises.values():
    #     print(pais)
    for pais, poblacion in Poblacion_paises.items():
             print(pais + " tiene " + str(poblacion)+ " Habitantes") 



if __name__ == "__main__":
    run()