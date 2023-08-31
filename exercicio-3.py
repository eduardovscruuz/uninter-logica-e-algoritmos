def cachorro_peso_base(): 
    while True: 
        try: 
            pesoC = int(input('Entre com o peso do cachorro:')) 
            if pesoC < 3: 
                return 40 
            elif 3 <= pesoC < 10: 
                return 50 
            elif 10 <= pesoC < 30: 
                return 60 
            elif 30 <= pesoC < 50: 
                return 70 
 
            else: 
                print('Não aceitamos cachorros tão grandes') 
                continue 
 
        except ValueError: 
            print('Você digitou um valor não numérico') 
 
def cachorro_pelo_multiplicador(): 
    while True: 
        peloC = input('Entre com o pelo do cachorro: \n' + 
                       'c - Pelo Curto \n' + 
                       'm - Pelo Médio \n' + 
                       'l - Pelo Longo \n' + 
                       '>>') 
        peloC = peloC.lower() #tudo para minúsculo 
        peloC = peloC.strip() #tira os espaços em branco no início e no final de uma string 
        if peloC == 'c': 
            return 1.00 
        elif peloC == 'm': 
            return 1.50 
        elif peloC == 'l': 
            return 2.0 
        else: 
            print('Digite uma das opções: c, m ou l') 
            continue 
 
def cachorro_extras(): 
    acumulador = 0 #acumula os extras que o cliente adicionar 
    while True: 
        extrasC = input ('Deseja adicionar mais algum serviço? \n' + 
                                '1 - Corte de Unhas - R$10,00 \n' + 
                                '2 - Escovar Dentes - R$12,00 \n' + 
                                '3 - Limpeza de Orelhas - R$15,00 \n' + 
                                '0 - Não desejo mais nada \n' + 
                                '>>') 
        if extrasC == '0': 
            return acumulador 
        elif extrasC == '1': 
            acumulador = acumulador + 10 
            continue 
        elif extrasC == '2': 
            acumulador = acumulador + 12 
            continue 
        elif extrasC == '3': 
            acumulador = acumulador + 15 
            continue 
        else: 
            print('Digite uma das opções: 0, 1, 2 ou 3') 
 
 
print('--------------- Bem-vindo ao Petshop do Eduardo Vieira de Souza Cruz ---------------') 
base = cachorro_peso_base() 
multiplicador = cachorro_pelo_multiplicador() 
extra = cachorro_extras() 
total = (base * multiplicador) + extra 
print('Total à pagar: R${:.2f} (Peso: R${:.2f}, Pelo: R${:.2f}, Adicional(is): R${:.2f})' .format(total, base, multiplicador, extra)) 
 