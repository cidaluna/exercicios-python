nota1 = float(input('Digite o primeiro número inteiro: '))
nota2 = float(input('Digite o segundo número inteiro: '))

media = (nota1 + nota2) / 2

print('****A media entre {} e {} é: {}' .format(nota1, nota2, media))

print('****Formatando a saída: A media entre {:.1f} e {:.1f} é: {:.1f}' .format(
    nota1, nota2, media))
