def tipoCambio(origen,destino,cantidad):
    usdApesos = 20.3179
    usdAEur = 0.89
    usdAYen = 113.47
    usdAReal= 3.79450
    if origen == "USD":
        if destino == "MXN":
            return cantidad * usdApesos
        elif destino == "EUR":
            return cantidad * usdAEur
        elif destino == "JPY":
            return cantidad * usdAYen
        elif destino == "BRL":
            return cantidad * usdAReal
        elif destino == "USD":
            return cantidad
        else:
            print("Asi no jala la moneda destino: "+ destino + "no existe")
            return 0
    if destino == "USD":
        if origen == "MXN":
            return cantidad / usdApesos
        elif origen == "EUR":
            return cantidad / usdAEur
        elif origen == "JPY":
            return cantidad / usdAYen
        elif origen =="BRL":
            return cantidad / usdAReal
        elif origen == "USD":
            return cantidad
        else:
            print("Asi no jala la moneda origen: "+ origen + " no existe")
            return 0
    else:
        return tipoCambio("USD",destino,tipoCambio(origen,"USD",cantidad))

print("USD 20,000 es igual a: " + str(tipoCambio("USD","MXN",20000))+ " pesos")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","USD",20000))+ " USD")
print("$ 20,000 pesos es igual a: " + str(tipoCambio("MXN","EUR",20000))+ " EUR")
print("20,000 EUR es igual a: " + str(tipoCambio("EUR","MXN",20000))+ " Pesos")
print("20,000 JPY es igual a: " + str(tipoCambio("JPY","MXN",20000))+ " Pesos")
print("20,000 Real es igual a : " + str(tipoCambio("BRL","MXN",20000))+ "Pesos")


