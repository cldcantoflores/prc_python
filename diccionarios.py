def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,

    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises ={
        'Argentina':42563454,
        'Brasil': 210357298,
        'Colombia': 50748247,
    }
 
    #print (poblacion_paises['Argentina'])

    # for pais in poblacion_paises.keys():
    #     print (pais)

    # for pais in poblacion_paises.values():
    #     print (pais)

    for pais, poblacion in poblacion_paises.items():
        print (pais+': '+str(poblacion))


if __name__ == '__main__':
    run()