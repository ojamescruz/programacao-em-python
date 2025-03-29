# Lista de Supermercado

# Método 1

print('Método 1')

produtos = ['arroz', 'feijão','ervilha', 'ração']
valores = [10.0,5.0,2.0,50.0]
 
print('produtos', produtos)

carrinho = []
meu_total = []


escolha1 = int(input('Id do produto'))
escolha2 = int(input('Id do produto'))
escolha3 = int(input('Id do produto'))


carrinho = [produtos[escolha1], produtos[escolha2],produtos[ escolha3]]
meu_total = [valores[escolha1], valores[escolha2],valores[ escolha3]]


total = meu_total[0] + meu_total[1]+meu_total[2]


print('Seus produtos', carrinho)
print('Valores dos seus produtos', meu_total)
print('*******************************************')
print('R$', total)

print("----------------------------")
print('Obrigada volte sempre')
print()
print()
print()




# Método 2

print('Método 2')

produtos = ['arroz', 'feijão','ervilha', 'ração']
valores = [10.0,5.0,2.0,50.0]
 
print('produtos', produtos)

carrinho = []
meu_total = []


escolha1 = int(input('Id do produto'))
escolha2 = int(input('Id do produto'))
escolha3 = int(input('Id do produto'))

carrinho.append(produtos[escolha1])
carrinho.append(produtos[escolha2])
carrinho.append(produtos[escolha3])

meu_total.append(valores[escolha1])
meu_total.append(valores[escolha2])
meu_total.append(valores[escolha3])

total = meu_total[0] + meu_total[1]+meu_total[2]


print('Seus produtos', carrinho)
print('Valores dos seus produtos', total)
print('*******************************************')
print('R$', total)

print("----------------------------")
print('Obrigada volte sempre')