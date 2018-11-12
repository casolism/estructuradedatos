def tipoCambio(dolares):
    return dolares * 20.3179

def tipoCambioPesos(pesos):
    return pesos / 20.3179

print("USD 20,000 es igual a: " + str(tipoCambio(20000))+ " pesos")
print("$ 20,000 pesos es igual a: " + str(tipoCambioPesos(20000))+ " USD")

