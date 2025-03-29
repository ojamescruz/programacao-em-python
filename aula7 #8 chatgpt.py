# Estrutura do e-commerce usando dicionários
ecommerce = {
    "produtos": {
        "livros": {
            "Produto1": {"nome": "O Senhor dos Anéis", "preço": 60.0},
            "Produto2": {"nome": "Harry Potter e a Pedra Filosofal", "preço": 50.0}
        },
        "tablets": {
            "Produto1": {"nome": "iPad Air", "preço": 3000.0},
            "Produto2": {"nome": "Samsung Galaxy Tab", "preço": 1200.0}
        },
        "fones_de_ouvido": {
            "Produto1": {"nome": "AirPods Pro", "preço": 1200.0},
            "Produto2": {"nome": "JBL Tune 500BT", "preço": 300.0}
        }
    },
    "carrinho": []
}

# Função para comprar um produto
def comprar(produto_tipo, produto_nome):
    produto = ecommerce["produtos"].get(produto_tipo, {}).get(produto_nome)
    if produto:
        ecommerce["carrinho"].append(produto)
        print(f"Você adicionou {produto['nome']} ao seu carrinho.")
    else:
        print("Produto não encontrado!")

# Função para pagar a compra
def pagar():
    if not ecommerce["carrinho"]:
        print("Seu carrinho está vazio! Adicione produtos para comprar.")
        return

    total = sum(item["preço"] for item in ecommerce["carrinho"])
    print(f"Valor total da compra: R${total:.2f}")
    ecommerce["carrinho"].clear()  # Esvaziar o carrinho após o pagamento
    print("Compra finalizada com sucesso!")

# Função para exibir os produtos disponíveis
def exibir_produtos():
    print("\nProdutos disponíveis:")
    for categoria, produtos in ecommerce["produtos"].items():
        print(f"\n{categoria.capitalize()}:")
        for chave, produto in produtos.items():
            print(f"{produto['nome']} - R${produto['preço']:.2f}")

# Exemplo de uso
def main():
    exibir_produtos()

    # Simulando compras
    comprar("livros", "Produto1")  # O Senhor dos Anéis
    comprar("tablets", "Produto2")  # Samsung Galaxy Tab
    comprar("fones_de_ouvido", "Produto1")  # AirPods Pro

    # Finalizando a compra
    pagar()

# Executa o e-commerce
if __name__ == "__main__":
    main()
