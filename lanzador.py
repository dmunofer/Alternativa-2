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

        ej3.count_patterns('A',4)

    if ejercicio==4:

        ej4.fibonacci(2000000)

    if ejercicio==5:

        mensaje=input('Introduce el mensaje que quieras encriptar')
        clave= input('Introduce la clave')
        encriptado= ej5.encriptar(mensaje,clave)
        ej5.desencriptar(encriptado,clave)



    else:
        print('Número de ejercicio incorrecto.(dDebe ser 1,2,3,4 o 5)')