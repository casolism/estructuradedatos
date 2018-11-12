def TipoCambio(dolares):
    return dolares * 20.3179

def TipoCambioPesos(Pesos):
    return Pesos / 20.3179

print("USD 20,000 es igual a: " + str(TipoCambio(20000))+" pesos")
print("$ 20,000 pesos es igual a: " + str(TipoCambioPesos(20000))+" USD")
