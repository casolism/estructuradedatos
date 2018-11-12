def tipoCambio(origen,destino,cantidad):
    usdApesos = 20.3179
    usdAEur = 0.89
    if origen == "MXN":
        if destino == "USD":
            return cantidad / usdApesos
        else:
            return tipoCambio("USD","EUR",tipoCambio("MXN","USD",cantidad))
    elif origen == "USD":
        if destino == "MXN":
            return cantidad * usdApesos
        else:
            return cantidad * usdAEur
    else:
        if destino == "MXN":
            return tipoCambio("USD","MXN",tipoCambio("EUR","USD",cantidad))
        else:
            return cantidad / usdAEur

print("USD 20,000 es igual a: " + str(tipoCambio("USD","MXN",20000))+ " pesos")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","USD",20000))+ " USD")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","EUR",20000))+ " EUR")
print("$ 20,000 EUR es igual a: " + str(tipoCambio("EUR","MXN",20000))+ " Pesos")

