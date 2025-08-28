print('**********Calculadora em Python**********\n')
print('Selecione o número da operação desejada:\n')
print('1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n')
opcao = int(input('Digite sua opção (1/2/3/4): '))
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if opcao == 1:
    resultado = primeiro_numero + segundo_numero
    print('Resultado:',resultado)
elif opcao == 2:
    resultado = primeiro_numero - segundo_numero
    print('Resultado:',resultado)
elif opcao == 3:
    resultado = primeiro_numero * segundo_numero
    print('Resultado:',resultado)
elif opcao == 4:
    resultado = primeiro_numero / segundo_numero
    print('Resultado:',resultado)
else:
    print('Insira uma opção válida')


