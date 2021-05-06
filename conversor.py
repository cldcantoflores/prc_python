def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos "+tipo_pesos+" tienes? "))
    dolares = round(pesos / valor_dolar,2)
    dolares = str(dolares)
    print("Tienes "+ " USD$ "+ dolares)



menu="""
Bienvenido al cursos de monedas
 
1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opción
"""

opcion = int(input(menu))

if opcion==1:
    conversor("colombianos",3875) 

elif opcion==2:
    conversor("argentinos",65) 

elif opcion ==3:
    conversor("mexicanos",24) 

else:
    print("Ingresa una opción correcta, por favor")
