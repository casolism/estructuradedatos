def tipocambio (dolares):
    return dolares * 20.3179

def tipocambioPesos(pesos):
    return pesos / 20.3179

print ("usd 20,000 es igual a: " +  str (tipocambio(20000)) + " pesos")
print ("$ 20000 pesos es igual a: " + str (tipocambioPesos(20000)) + "USD")

