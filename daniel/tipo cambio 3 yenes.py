def tipoCambio(origen,destino,cantidad):
    usdApesos = 20.3179
    usdAEur = 0.89
    usdAYen = 113.47
    if origen == "USD":
        if destino == "MXN":
            return cantidad * usdApesos
        elif destino == "EUR":
            return cantidad * usdAEur
        elif destino == "JPY":
            return cantidad * usdAYen
        else:
            return cantidad
    if destino == "USD":
        if origen == "MXN":
            return cantidad / usdApesos
        elif origen == "EUR":
            return cantidad / usdAEur
        elif origen == "JPY":
            return cantidad / usdAYen
        else:
            return cantidad
    else:
        return tipoCambio("USD",destino,tipoCambio(origen,"USD",cantidad))

print("USD 20,000 es igual a: " + str(tipoCambio("USD","MXN",20000))+ " pesos")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","USD",20000))+ " USD")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","EUR",20000))+ " EUR")
print("20,000 EUR es igual a: " + str(tipoCambio("EUR","MXN",20000))+ " Pesos")
print("20,000 JPY es igual a: " + str(tipoCambio("JPY","MXN",20000))+ " Pesos")
