print('Bem-vindo a loja do João Pedro Flauzino Nascimento')  # Identificador pessoal

valorProduto = float(input('Entre com o valor do produto: '))  # Variável vai receber o valor do produto
quantidade = int(input('Entre com a quantidade de produtos: '))  # Variável vai receber a quantidade do produto

subTotal = valorProduto * quantidade  # Vai receber a multiplicação entre o valor e quantidade de produtos

if 0 <= quantidade < 11:  # Caso a quantidade estiver entre 0 e 11 entra nesse if
    valorFinal = subTotal + 30  # Soma para descobrir o valor com o frete
elif 11 <= quantidade < 101:  # Caso a quantidade estiver entre 11 e 101 entra nesse elif
    valorFinal = subTotal + 60  # Soma para descobrir o valor com o frete
elif 101 <= quantidade < 1001:  # Caso a quantidade estiver entre 101 e 1001 entra nesse elif
    valorFinal = subTotal + 120  # Soma para descobrir o valor com o frete
else: # Caso a quantidade estiver acima de 1001 entra nesse else
    valorFinal = subTotal + 240  # Soma para descobrir o valor com o frete

valorFrete = valorFinal - subTotal  # Faz a subtração para descobrir o valor do frete cobrado.

print('O valor sem frete foi: R$ {:.2f}'.format(subTotal))  # Imprime o valor sem o frete.
print('O valor com Frete foi: R$ {:.2f} (frete de R$ {:.2f})'.format(valorFinal, valorFrete))  # Imprime o valor com o frete, e o valor do frete.


