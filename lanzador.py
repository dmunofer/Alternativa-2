import sys

sys.path.insert(0,"/Users/smite/Documents/GitHub/Alternativa2/Ejercicio1/ej1")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Alternativa2/Ejercicio2/ej2")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Alternativa2/Ejercicio3/ej3")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Alternativa2/Ejercicio2/ej4")
sys.path.insert(0,"/Users/smite/Documents/GitHub/Alternativa2/Ejercicio3/ej5")


from Ejercicio1 import ej1
from Ejercicio2 import ej2
from Ejercicio3 import ej3
from Ejercicio4 import ej4
from Ejercicio5 import ej5

def exe():
    ejercicio=input("Introduce el numero del ejercicio que quieras lanzar:")

    if ejercicio==1:
        sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
        ej1.resolver(sudoku)



    if ejercicio==2:
        ej2.expand("(x+1)^2")      
        ej2.expand("(p-1)^3")      
        ej2.expand("(2f+4)^6")     
        ej2.expand("(-2a-4)^0")    
        ej2.expand("(-12t+43)^2")  
        ej2.expand("(r+0)^203")   
        ej2.expand("(-x-1)^2") 

    if ejercicio==3:

        maravillas=[{'Nombre': 'Gran Muralla China', 'Pais': 'China', 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Coliseo de Roma' , 'Pais': 'Italia' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Ciudad de Petra', 'Pais': 'Jordania ' , 'Tipo': 'ARQUITECTURA'}, {'Nombre': 'Bahía de Ha Long', 'Pais': 'Vietnam' , 'Tipo': 'NATURAL'},
            {'Nombre': 'Isla Jeju', 'Pais': 'Corea Sur' , 'Tipo': 'NATURAL'}, {'Nombre': 'Machu Picchu', 'Pais': 'Peru' , 'Tipo': 'ARQUITECTURA'},
            {'Nombre': 'Taj Mahal', 'Pais': 'India', 'Tipo':'ARQUITECTURA'}]

        dist = [['Gran Muralla China', 'Coliseo de Roma', 7462], ['Coliseo de Roma','Machu Picchu', 10709], ['Gran Muralla China', 'Ciudad de Petra', 6318],
        ['Gran Muralla China', 'Machu Picchu', 16888], ['Gran Muralla China', 'Taj Mahal', 7470], ['Ciudad de Petra','Taj Mahal', 4296],
        ['Coliseo de Roma','Ciudad de Petra', 3673], ['Bahía de Ha Long', 'Isla Jeju', 2362 ],['Machu Picchu', 'Taj Mahal', 17041],
        ['Coliseo de Roma','Taj Mahal', 6640], ['Ciudad de Petra', 'Machu Picchu',  12441]]

        ej3.paisambasmaravillas(maravillas)
        ej3.paismismasmaravillasnatu(maravillas)
        ej3.paismismasmaravillasarq(maravillas)

    else:
        print('Número de ejercicio incorrecto.(dDebe ser 1,2 o 3)')