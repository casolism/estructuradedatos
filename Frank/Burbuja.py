def burbuja (numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if (numeros[j]>numeros[j+1]):
                aux=numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux
    return numeros
        
#numDesordenados=[2,8,3,5,10,22,56,48,51,4,2.5]
numDesordenados=['Pepe','Toño','Francisco','Jorge','Raul']
print('Numeros Desordenados')
print(numDesordenados)
numOrdenados=burbuja(numDesordenados)
print('Numeros Ordenados')
print(numOrdenados)
    
