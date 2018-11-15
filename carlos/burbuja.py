#Funcion de ordenamiento
def burbuja(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if (numeros[j]>numeros[j+1]):
                aux = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = aux
    return numeros

#Programa principal
#numDesordenados = [2,12,33,11,11,40,34,8,3,5,10,12,1]
numDesordenados = ["Carlos","Ana","Juan","Jorge"]
print ("Numeros desordenados")
print (numDesordenados)
numOrdenados = burbuja(numDesordenados)
print ("Numeros ordenados")
print (numOrdenados)
