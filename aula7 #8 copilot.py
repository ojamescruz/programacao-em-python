# Estrutura de dicionários com os produtos e seus preços
produtos = {
    "livros": 50.00,
    "tablets": 500.00,
    "fones de ouvido": 100.00
}

# Carrinho de compras
carrinho = {}

# Função para comprar produtos
def comprar(produto, quantidade):
    if produto in produtos:
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade
        print(f"{quantidade} unidade(s) de {produto} adicionada(s) ao carrinho.")
    else:
        print("Produto não encontrado.")

# Função para pagar e mostrar o valor total da compra
def pagar():
    if not carrinho:
        print("O carrinho está vazio.")
        return

    total = 0
    print("Resumo da compra:")
    for produto, quantidade in carrinho.items():
        valor = produtos[produto] * quantidade
        total += valor
        print(f"{produto.capitalize()} - Quantidade: {quantidade} - Preço: R${valor:.2f}")
    print(f"Valor total: R${total:.2f}")
    print("Pagamento realizado com sucesso!")
    carrinho.clear()

# Exemplo de uso
comprar("livros", 2)
comprar("tablets", 1)
comprar("fones de ouvido", 3)
pagar()
