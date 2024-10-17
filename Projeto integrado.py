# Estrutura de dados para Produtos, Categorias e Movimentações
produtos = []
categorias = []
movimentacoes = []
contador_produtos = 0
contador_categorias = 0
contador_movimentacoes = 0


# Função para cadastrar um produto
def cadastrar_produto():
    global contador_produtos
    contador_produtos += 1

    nome = input("Nome do Produto: ")
    categoria_id = int(input("ID da Categoria: "))
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    # Produto é representado por um dicionário
    produto = {
        "id": contador_produtos,
        "nome": nome,
        "categoria_id": categoria_id,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


# Função para cadastrar uma categoria
def cadastrar_categoria():
    global contador_categorias
    contador_categorias += 1

    nome = input("Nome da Categoria: ")

    # Categoria é representada por um dicionário
    categoria = {
        "id": contador_categorias,
        "nome": nome
    }

    categorias.append(categoria)
    print("Categoria cadastrada com sucesso!")


# Função para consultar um produto pelo ID
def consultar_produto_por_id(id):
    for produto in produtos:
        if produto["id"] == id:
            print(
                f"ID: {produto['id']}, Nome: {produto['nome']}, Categoria ID: {produto['categoria_id']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")
            return
    print("Produto não encontrado!")


# Função para consultar um produto por nome
def consultar_produto_por_nome(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(
                f"ID: {produto['id']}, Nome: {produto['nome']}, Categoria ID: {produto['categoria_id']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")
            return
    print("Produto não encontrado!")


# Função para consultar produtos por categoria
def consultar_produto_por_categoria(categoria_id):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            print(f"Produtos da Categoria {categoria['nome']}:")
            for produto in produtos:
                if produto["categoria_id"] == categoria_id:
                    print(
                        f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")
            return
    print("Categoria não encontrada!")


# Função para registrar uma movimentação (entrada ou saída de estoque)
def registrar_movimentacao():
    global contador_movimentacoes
    contador_movimentacoes += 1

    produto_id = int(input("ID do Produto: "))
    quantidade = int(input("Quantidade: "))
    tipo_movimentacao = input("Tipo de Movimentação (E para entrada, S para saída): ").upper()
    data = input("Data (DD/MM/AAAA): ")

    # Verifica se o produto existe
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        if tipo_movimentacao == 'E':  # Entrada de produtos no estoque
            produto["quantidade"] += quantidade
        elif tipo_movimentacao == 'S':  # Saída de produtos do estoque
            if produto["quantidade"] >= quantidade:
                produto["quantidade"] -= quantidade
            else:
                print("Quantidade insuficiente no estoque!")
                return
        else:
            print("Tipo de movimentação inválido!")
            return

        # Registra a movimentação
        movimentacao = {
            "id": contador_movimentacoes,
            "produto_id": produto_id,
            "quantidade": quantidade,
            "tipo_movimentacao": tipo_movimentacao,
            "data": data
        }
        movimentacoes.append(movimentacao)
        print("Movimentação registrada com sucesso!")
    else:
        print("Produto não encontrado!")


# Função para gerar relatório de estoque
def gerar_relatorio_estoque():
    print("Relatório de Estoque:")
    for produto in produtos:
        print(
            f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")


# Função para consultar o histórico de movimentações de um produto
def consultar_movimentacoes(produto_id):
    print(f"Movimentações do Produto ID {produto_id}:")
    for movimentacao in movimentacoes:
        if movimentacao["produto_id"] == produto_id:
            tipo = "Entrada" if movimentacao["tipo_movimentacao"] == 'E' else "Saída"
            print(
                f"ID: {movimentacao['id']}, Quantidade: {movimentacao['quantidade']}, Tipo: {tipo}, Data: {movimentacao['data']}")


# Menu de opções
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Categoria")
        print("2. Cadastrar Produto")
        print("3. Consultar Produto por ID")
        print("4. Consultar Produto por Nome")
        print("5. Consultar Produto por Categoria")
        print("6. Registrar Movimentação")
        print("7. Gerar Relatório de Estoque")
        print("8. Consultar Movimentações")
        print("9. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_categoria()
        elif opcao == 2:
            cadastrar_produto()
        elif opcao == 3:
            id = int(input("Digite o ID do Produto: "))
            consultar_produto_por_id(id)
        elif opcao == 4:
            nome = input("Digite o Nome do Produto: ")
            consultar_produto_por_nome(nome)
        elif opcao == 5:
            categoria_id = int(input("Digite o ID da Categoria: "))
            consultar_produto_por_categoria(categoria_id)
        elif opcao == 6:
            registrar_movimentacao()
        elif opcao == 7:
            gerar_relatorio_estoque()
        elif opcao == 8:
            produto_id = int(input("Digite o ID do Produto: "))
            consultar_movimentacoes(produto_id)
        elif opcao == 9:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Chamar o menu para iniciar o sistema
menu()
