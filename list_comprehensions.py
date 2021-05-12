def run ():
    #squares=[]

    # for i in range(1,101):
    #     if i%3!=0:
    #         squares.append(i**2)
    
    #squares =[i**2 for i in range(1,101) if i%3!=0 ]

    #print(squares)

    #todos los multiplos de 4 que sean multiplos de 6 y de 9 del 1 al 10000

    mul4 = [i for i in range(1,10001) if i%4==0 and i%9==0]
    print(mul4)

if __name__ =='__main__':
    run()