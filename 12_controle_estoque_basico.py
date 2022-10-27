registroDeEntradas = int(input('Quantas bolsas de sangue entraram? '))

registroDeSaidas = int(input('Quantas bolsas de sangue sairam? '))

estoqueAtual = registroDeEntradas - registroDeSaidas

mlAtual = estoqueAtual * 500

print('Tivemos {} bolsas de entrada e {} bolsas de saida, logo o estoque atual é de {} bolsa(s) de sangue ({} ml.)'.format(
    registroDeEntradas, registroDeSaidas, estoqueAtual, mlAtual))
