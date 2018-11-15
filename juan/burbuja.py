#funcion de ordenamiento 
def burbuja(numeros):
    i = 0
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):    
            if (numeros[j]>numeros[j+1]):
                aux= numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1]=aux
        
    return numeros

#programa principal
numDesordenados = [2,8,3,5,10,15,6,9,50,10,4,1,0,90,7]
print("numeros desordenados")
print(numDesordenados)
numOrdenados = burbuja(numDesordenados)
print("num urdenados")
print (numOrdenados)
