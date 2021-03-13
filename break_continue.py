def run():

    texto = input("Escribe un texto: ")
    texto  = texto.lower()
    largo = len(texto)
    contador = 0
    
    while contador < largo:
       print(texto[contador])
       
       if texto[contador]== 'o':
            break
        
       contador +=1    
    

if __name__ == '__main__':
    run()