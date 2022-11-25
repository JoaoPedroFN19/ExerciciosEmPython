acumulador = 0

print('Bem-vindo a Sorveteria do João Pedro Flauzino Nascimento')  # Identificador
print('----------------------------------------- CARDÁPIO ---------------------------------------------')
print('| CÓDIGO  |      DESCRIÇÃO       | TAMANHO P (500ML) | TAMANHO M (1000ML) | TAMANHO G (2000ML) |')
print('|    TR   | SABORES TRADICIONAIS |     R$   6,00     |      R$  10,00     |     R$  18,00      |')
print('|    ES   | SABORES ESPECIAIS    |     R$   7,00     |      R$  12,00     |     R$  21,00      |')
print('|    PR   | SABORES PREMIUM      |     R$   8,00     |      R$  14,00     |     R$  24,00      |')
print('------------------------------------------------------------------------------------------------')

while True:
    tamanho = input('Entre com o TAMANHO do pote desejado (P/G/M): ')  # Recebe o tamanho do pote
    tamanho = tamanho.upper()  # Resolve o problema de digitar minuscula
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':  # Para caso o usúario escolher algo inválido
        print('!!!!! TAMANHO INVÁLIDO(S) !!!!!')
        continue  # Se o usuário digitar algo inválido volta para o começo while

    codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ')  # Recebe o código do pedido
    codigo = codigo.upper()  # Resolve o problema de digitar minuscula
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':  # Para caso o usúario escolher algo inválido
        print('!!!!! CÓDIGO INVÁLIDO(S) !!!!!')
        continue  # Se o usuário digitar algo inválido volta para o começo while

    if codigo == 'TR' and tamanho == 'P':  # Se o pedido for esse, entra nesse if
        print('Você pediu um sorvete sabor TRADICIONAL tamanho P de R$ 6,00')
        acumulador = acumulador + 6  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'TR' and tamanho == 'M':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor TRADICIONAL tamanho M de R$ 10,00')
        acumulador = acumulador + 10  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'TR' and tamanho == 'G':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor TRADICIONAL tamanho G de R$ 18,00')
        acumulador = acumulador + 18  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'ES' and tamanho == 'P':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor ESPECIAIS tamanho P de R$ 7,00')
        acumulador = acumulador + 7  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'ES' and tamanho == 'M':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor ESPECIAIS tamanho M de R$ 12,00')
        acumulador = acumulador + 12  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'ES' and tamanho == 'G':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor ESPECIAIS tamanho G de R$ 21,00')
        acumulador = acumulador + 21  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'PR' and tamanho == 'P':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor PREMIUM tamanho P de R$ 8,00')
        acumulador = acumulador + 8  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'PR' and tamanho == 'M':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor PREMIUM tamanho M de R$ 14,00')
        acumulador = acumulador + 14  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    elif codigo == 'PR' and tamanho == 'G':  # Se o pedido for esse, entra nesse elif
        print('Você pediu um sorvete sabor PREMIUM tamanho G de R$ 24,00')
        acumulador = acumulador + 24  # Pegue o valor que tinha no acumulador e soma com o preço do pedido

    pedirMais = input(' Deseja pedir mais alguma coisa? (S/ Digite outra tecla: )')  # Recebe a escolha de pedir mais ou não.
    pedirMais = pedirMais.upper()
    if pedirMais == 'S':
        continue
    else:
        print('O total a ser pago é: R${:.2f}'.format(acumulador))  # Mostra o valor total dos pedidos.
        break
