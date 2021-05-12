def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"fisrtname":"Facundo","lastname":"García"}

    super_list =[
        {"fisrtname":"Facundo","lastname":"García"},
        {"fisrtname":"Facundo2","lastname":"García2"},
        {"fisrtname":"Facundo3","lastname":"García3"},
        {"fisrtname":"Facundo4","lastname":"García4"},
        {"fisrtname":"Facundo4","lastname":"García5"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-2,-1,-0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }


    for key,value in super_dict.items():
        print(key,' - ',value)


    for i in super_list:
        print(i.items())


if __name__=='__main__':
    run()