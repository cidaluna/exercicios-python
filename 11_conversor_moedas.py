dimdimReal = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolar = 5.32
euro = 5.29

converteDolar = dimdimReal / dolar
converteEuro = dimdimReal / euro

print('**** Com este valor R$ {:.2f}, você pode comprar US$ {:.2f} dólares.'.format(
    dimdimReal, converteDolar))

print('**** Com este valor R$ {:.2f}, você pode comprar € {:.2f} euros.'.format(
    dimdimReal, converteEuro))
