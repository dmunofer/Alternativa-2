def encriptar(mensaje, clave):
    rail = [['\n' for i in range(len(mensaje))]
                for j in range(clave)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(mensaje)):
        if (row == 0) or (row == clave - 1):
            dir_down = not dir_down
        rail[row][col] = mensaje[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(clave):
        for j in range(len(mensaje)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def desencriptar(encriptado, clave):
    rail = [['\n' for i in range(len(encriptado))]
                for j in range(clave)]

    dir_down = None
    row, col = 0, 0
     

    for i in range(len(encriptado)):
        if row == 0:
            dir_down = True
        if row == clave - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         

        if dir_down:
            row += 1
        else:
            row -= 1
             

    index = 0
    for i in range(clave):
        for j in range(len(encriptado)):
            if ((rail[i][j] == '*') and
               (index < len(encriptado))):
                rail[i][j] = encriptado[index]
                index += 1
         
  
    result = []
    row, col = 0, 0
    for i in range(len(encriptado)):
         
        
        if row == 0:
            dir_down = True
        if row == clave-1:
            dir_down = False
             
       
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 