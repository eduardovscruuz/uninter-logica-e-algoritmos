print('Bem-vindo à Sorveteria do Eduardo Vieira de Souza Cruz') 
print('------------------------------------CARDÁPIO------------------------------------') 
print('Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |') 
print('     1      |        R$ 6,00         |       R$ 7,00      |       R$ 8,00       |') 
print('     2      |        R$ 10,00        |       R$ 12,00     |       R$ 14,00      |') 
print('     3      |        R$ 14,00        |       R$ 17,00     |       R$ 20,00      |') 
 
acumulador = 0 # valor a pagar será acumulado aqui 
 
while True: 
    sabor = input('Entre com o sabor desejado (tr/es/pr):') 
    if sabor != 'tr' and sabor != 'es' and sabor != 'pr': 
        print('Sabor inválido. Tente novamente') 
        continue  # se usuário digitar algo inválido volta para o começo do while 
 
    bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3):') 
    if bolas != '1' and bolas != '2' and bolas != '3': 
        print('Número de bolas de sorvete inválido. Tente novamente') 
        continue # se usuário digitar algo inválido volta para o começo do while 
 
    if bolas == '1' and sabor == 'tr': 
        print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$6,00') 
        acumulador = acumulador + 6 
    elif bolas == '2' and sabor == 'tr': 
        print('Você pediu 2 bolas de sorvete no sabor TRADICIONAL: R$10,00') 
        acumulador = acumulador + 10 
    elif bolas == '3' and sabor == 'tr': 
        print('Você pediu 3 bolas de sorvete no sabor TRADICIONAL: R$14,00') 
        acumulador = acumulador + 14 
    elif bolas == '1' and sabor == 'pr': 
        print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$7,00') 
        acumulador = acumulador + 7 
    elif bolas == '2' and sabor == 'pr': 
        print('Você pediu 2 bolas de sorvete no sabor PREMIUM: R$12,00') 
        acumulador = acumulador + 12 
    elif bolas == '3' and sabor == 'pr': 
        print('Você pediu 3 bolas de sorvete no sabor PREMIUM: R$17,00') 
        acumulador = acumulador + 17 
    elif bolas == '1' and sabor == 'es': 
        print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$8,00') 
        acumulador = acumulador + 8 
    elif bolas == '2' and sabor == 'es': 
        print('Você pediu 2 bolas de sorvete no sabor ESPECIAL: R$14,00') 
        acumulador = acumulador + 14 
    elif bolas == '3' and sabor == 'es': 
        print('Você pediu 3 bolas de sorvete no sabor ESPECIAL: R$20,00') 
        acumulador = acumulador + 20 
 
 
    pedir_mais = input('Deseja mais algum sorvete (s/digite outra tecla)?') 
    pedir_mais = pedir_mais.upper() # resolve o problema de digitar 's' e 'S' 
    if pedir_mais == 'S': 
        continue 
    else: 
        print('O valor total a ser pago: R${:.2f}' .format(acumulador)) 
        break # para o loop do programa