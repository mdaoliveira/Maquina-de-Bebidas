bebidas = [[1, 'Coca-cola', 3.75, 2],
 [2, 'Pepsi', 3.67, 5],
 [3, 'Monster', 9.96, 1],
 [4, 'Café', 1.25, 100],
 [5, 'Redbull', 13.99, 2]]
#Exibição da matriz com as bebidas
for i in bebidas:
    print(i, end="")
    print()
#Função que verifica se a bebida está disponível no estoque
def verificar_estoque(pedido_cliente):
    indice_bebida = pedido_cliente - 1
    #Impede que o usuário insira uma ID que não seja de 1 a 5
    if pedido_cliente == 0 or pedido_cliente > 5:
        print('Pedido inválido.')
    elif bebidas[indice_bebida][3] == 0:
        print('Não há estoque.')
    elif bebidas[indice_bebida][3] != 0:
        print('Há estoque disponível. O estoque é de',bebidas[indice_bebida][3])

#Verifica o valor da bebida, verifica se o valor inserido pelo usuário é válido e calcula o troco
def pagamento_bebida(pedido_cliente):
    indice_bebida = pedido_cliente - 1
    preco_bebida = bebidas[indice_bebida][2]
    print('O valor é de R$' + str(preco_bebida)+'\n')
    valor_pago = -1
    while valor_pago < 0:
        valor_pago = float(input('Insira um valor válido em dinheiro a ser pago: '))
        if valor_pago >= preco_bebida:
            print('Valor inserido R$', valor_pago)
        else:
            print('Valor inválido')
            valor_pago = -1
    global troco
    troco = valor_pago - preco_bebida
    print('O troco a ser dado é R$ %.2f'%(troco))

#Calcula o troco e especifica as notas/moedas a serem devolvidas
def dar_troco(troco):
    #Lista de notas e moedas presentes na máquina para troco
    notas_ou_moedas = [20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.01]
    for i in range(len(notas_ou_moedas)):
        if troco >= notas_ou_moedas[i]:
            indice = 0
            while troco >= notas_ou_moedas[i]:
                troco = float('%.2f'%(troco - notas_ou_moedas[i]))
                indice += 1
            if troco > 1:
                print(indice, 'nota(s) de', notas_ou_moedas[i])
            else:
                print(indice, 'moeda(s) de', notas_ou_moedas[i])

#Atualiza o estoque após a compra
def atualizar_estoque(pedido_cliente):
    indice_bebida = pedido_cliente - 1
    pedido_estoque = bebidas[indice_bebida][3]
    bebidas[indice_bebida][3] = pedido_estoque - 1
    print('Estoque atualizado do produto',bebidas[indice_bebida][1],':',bebidas[indice_bebida][3])
    pedido_cliente = 0

#Chama as funções para que o código seja executado, desde que a ID informada pelo usuário seja válida (de 1 a 5)
while pedido_cliente == 0 or pedido_cliente > 5:
    pedido_cliente = int(input('Insira o código da bebida desejada: '))
    verificar_estoque(pedido_cliente)
    pagamento_bebida(pedido_cliente)
    dar_troco(troco)
    atualizar_estoque(pedido_cliente)