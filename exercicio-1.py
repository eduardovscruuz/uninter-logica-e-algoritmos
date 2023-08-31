print('Bem-vindo à Loja do Eduardo Vieira de Souza Cruz') 
 
valor_produto = float(input('Entre com o valor do produto: ')) 
qtd_produto = int(input('Entre com a quantidade do produto: ')) 
desconto_produto = 0 
 
if qtd_produto < 200: #se a quantidade for menor que 200 
    desconto_produto = 0.00 #sem desconto 
elif 200 <= qtd_produto < 1000: #se a quantidade for maior ou igual 200 e menor que 1000 
    desconto_produto = 0.05 #desconto de 15% 
elif 1000 <= qtd_produto < 2000: #se a quantidade for maior ou igual 200 e menor que 1000 
    desconto_produto = 0.10 #desconto de 15% 
else: 
    desconto_produto = 0.15 #desconto de 15% 
 
total_sem_desconto = valor_produto * qtd_produto 
print('O valor total SEM desconto: R${:.2f}' .format(total_sem_desconto)) 
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto 
print('O valor total COM desconto: R${:.2f}' .format(total_com_desconto))
