def TipoCambio(dolares):
    return dolares * 20.3179
def TipoCambioPesos(pesos):
    return pesos / 20.3179

print ("USD 20,000 es igual a: "+ str(TipoCambio(20000))+ " pesos")
print ("$ 20,000 pesos es igual a: "+ str(TipoCambioPesos(20000))+ " USD ")
