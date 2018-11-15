#funcion Ordenamiento
def burbuja(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]
                numeros[j]= numeros[j+1]
                numeros[j+1] = aux
    return numeros    

#programa principal
numDesordenados = [2,8,3,5,10]
numOrdenados = burbuja(numDesordenados)
print (numOrdenados)
