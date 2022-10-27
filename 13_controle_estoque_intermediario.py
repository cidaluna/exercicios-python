
import numbers


opcao = 0
registroDeEntradas = 0
registroDeSaidas = 0
estoqueAtual = 0
entr = 0
said = 0
while opcao != 4:
    print('''
    *** Controle de Estoque de Bolsas de Sangue ***
    [1] Registrar entrada
    [2] Registrar saída
    [3] Consultar estoque atual de bolsa(s) e ml
    [4] Sair
    ''')
    opcao = int(input('Digite o número da opção que deseja realizar: '))
    if opcao == 1:
        registroDeEntradas = int(input('Quantas bolsas de sangue ENTRARAM ? '))
        print(' ---> Registrado {} bolsas de sangue de entrada!'.format(registroDeEntradas))
        entr += registroDeEntradas
    elif opcao == 2:
        if estoqueAtual > 0:
            registroDeSaidas = int(input('Quantas bolsas de sangue SAIRAM ? '))
            print(
                ' ---> Registrado {} bolsas de sangue de saída.'.format(registroDeSaidas))
            if registroDeSaidas > estoqueAtual:
                print(
                    'ATENÇÃO: O número de saídas nao pode ser maior que o número de estoque atual.')
            else:
                said += registroDeSaidas
        else:
            print('ATENÇÃO: O número de saídas deve ser correspondente ao estoque atual.')
    elif opcao == 3:
        estoqueAtual = entr - said
        mlAtual = estoqueAtual * 500
        print(' ---> Temos {} bolsa(s) de entrada e {} bolsa(s) de saída, logo o estoque atual é de {} bolsa(s) de sangue ({} ml.)'.format(
            entr, said, estoqueAtual, mlAtual))
        print('Total de entradas = {} '.format(entr))
        print('Total de saidas = {} '.format(said))
        print('ESTOQUE = {} '.format(estoqueAtual))
    elif opcao == 4:
        opcao = 4
    else:
        print('Opção inválida!')
print('Encerrando o programa')
