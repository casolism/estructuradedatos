def TipoCambio(origen,destino,cantidad):
    usdAPeso = 20.3179
    usdAEur = 0.89
    return dolares * 20.3179
if origen == "MXN":
    if destino == "USD":
        return cantidad / usdApesos
    else:
        return TipoCambio("USD","EUR",TipoCambio("MXN","USD",cantidad))
    elif origen == "USD":
        if destino == "MXN":
            return cantidad * usdApesos
        else:
            return cantidad * usdAEur
    else:
        if destino == "MXN":
            return tipodecambio("USD","MXN",TipodeCambio("EUR","USD",cantidad))
        else:
            return cantidad / usdAEur


print("USD 20,000 es igual a: " + str(TipoCambio("USD","MXN",20000))+" pesos")
print("$ 20,000 pesos es igual a: " + str(TipoCambiO("MXN","USD",20000))+ " USD")
print("$ 20,000 pesos es igual a: " + str(TipoCambio("MXN","EUR",20000))+ " EUR")
print("$ 20,000 EUR es igual a: " + str(TipoCambio("EUR","MXN",20000))+ "Pesos")
