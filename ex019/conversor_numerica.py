while True:


    num = int(input('Digite um numero inteiro: '))
    print('''Escolha uma das bases para conversão: 
        [ 1 ] converter para BINÁRIO
        [ 2 ] converter para OCTAL 
        [ 3 ] converter para HEXADECIMAL
        [ 4 ] Encerramento''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format, (num, bin(num)))
    elif opcao == 2:
        print('{} convertido para OCTAL é igual a {}'.format, (num, oct(num)))
    elif opcao == 3:
        print ('{} convertido para HEXADECIMAL é igual a {}'.format, (num , hex(num)))
    elif opcao == 4:
        print('Sistema encerrado!')
        break
    else:
        print('NUMERO INVALIDO!')
        
        