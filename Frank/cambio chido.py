def tipocambio(origen,destino,cantidad):
    USDpeso=20.3179
    USDeuro=0.89
    USDYen=
    USDReal=
    if origen=='MXN':
        if destino==USD
           return cantidad/USDpesos
        else:
           return tipocambio('USD','EUR',tipocambio('MXN','USD',cantidad))
    elif origen=='USD':
         if destino=='MXN':
            return cantidad*USDpeso
        else:
            return cantidad*USDeuro
    else:
        if destino=='MXN':
            return tipocambio('USD','MXN',tipocambio('EUR','USD',cantidad))
        else:
            return cantidad/USDeruo
print('USD 20,000 es igual a: '+str(tipocambio('USD','MXN',20,000))+ 'Pesos')
print('$20,000 pesos es igual a: '+str(tipocambio('MXN','USD',20,000))+ 'USD')                              
print('$20,000 pesos es igual a: '+str(tipocambio('MXN','EUR',20,000))+ 'EUR')
print('20,000 es igual a: '+str(tipocambio('EUR','MXN',20,000))+ 'Pesos')
print('20,000 es igual a: '
