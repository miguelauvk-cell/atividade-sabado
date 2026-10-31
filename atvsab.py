

compras = ["arroz", "feijão", "leite", "pão", "café"]

print("Lista original:", compras)

compras[2] = "suco"

print("Lista atualizada:", compras)




mochila = ["caderno", "caneta", "lápis", "borracha", "régua"]

objeto = input("\nDigite o objeto que deseja retirar: ")

if objeto in mochila:
    mochila.remove(objeto)
    print("Objeto removido!")
else:
    print("Objeto não encontrado!")

print("Mochila atualizada:", mochila)




tarefas = []

for i in range(5):
    tarefa = input("\nDigite uma tarefa: ")
    tarefas.append(tarefa)

print("Lista de tarefas:")

for i in range(len(tarefas)):
    print(i + 1, "-", tarefas[i])




jogadores = ["Lucas", "Pedro", "Marcos", "Rafael", "Bruno"]

print("\nJogadores:", jogadores)

posicao = int(input("Qual posição deseja substituir (1 a 5)? "))
novo = input("Digite o novo jogador: ")

if posicao >= 1 and posicao <= 5:
    jogadores[posicao - 1] = novo
    print("Lista atualizada:", jogadores)
else:
    print("Posição inválida!")




precos = [25.0, 80.0, 15.0, 120.0, 45.0]

promocao = []

for preco in precos:
    if preco > 50:
        novo_preco = preco * 0.90
        promocao.append(novo_preco)
    else:
        promocao.append(preco)

print("\nPreços originais:", precos)
print("Preços promocionais:", promocao)




palavras = ["sol", "computador", "casa", "programação", "pé", "python"]

palavras_grandes = []

for palavra in palavras:
    if len(palavra) >= 5:
        palavras_grandes.append(palavra)

print("\nPalavras grandes:", palavras_grandes)




convidados = []

for i in range(8):
    nome = input("\nDigite o nome do convidado: ")

    if nome not in convidados:
        convidados.append(nome)
    else:
        print("Convidado já cadastrado!")

print("Convidados cadastrados:")

for nome in convidados:
    print(nome)




palavras = []
palavras_a = []

for i in range(8):
    palavra = input("\nDigite uma palavra: ")
    palavras.append(palavra)

for palavra in palavras:
    if palavra[0].lower() == "a":
        palavras_a.append(palavra)

print("Todas as palavras:", palavras)
print("Palavras que começam com A:", palavras_a)


cores = ["azul", "verde", "amarelo", "vermelho", "preto"]

print("\nOrdem original:")

for i in range(len(cores)):
    print(cores[i])

print("Ordem contrária:")

for i in range(len(cores) - 1, -1, -1):
    print(cores[i])




jogos_joao = ["Minecraft", "FIFA", "Fortnite", "GTA", "Valorant"]

jogos_pedro = ["GTA", "Rocket League", "Minecraft", "CS", "Valorant"]

jogos_em_comum = []

for jogo in jogos_joao:
    if jogo in jogos_pedro:
        jogos_em_comum.append(jogo)

print("\nJogos em comum:", jogos_em_comum)



proibidas = ["spam", "propaganda", "golpe"]

palavras = []
bloqueadas = 0

for i in range(5):
    palavra = input("\nDigite uma palavra: ")
    palavras.append(palavra)

for palavra in palavras:
    if palavra in proibidas:
        print(palavra, "- BLOQUEADA")
        bloqueadas += 1
    else:
        print(palavra, "- PERMITIDA")

print("Quantidade bloqueada:", bloqueadas)




carrinho = []

while True:
    print("\n===== CARRINHO DE COMPRAS =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Mostrar carrinho")
    print("4 - Procurar produto")
    print("5 - Mostrar quantidade")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        produto = input("Digite o produto: ")
        carrinho.append(produto)
        print("Produto adicionado!")

    elif opcao == 2:
        produto = input("Digite o produto para remover: ")

        if produto in carrinho:
            carrinho.remove(produto)
            print("Produto removido!")
        else:
            print("Produto não encontrado!")

    elif opcao == 3:
        print("Produtos no carrinho:")

        for produto in carrinho:
            print("-", produto)

    elif opcao == 4:
        produto = input("Digite o produto para procurar: ")

        if produto in carrinho:
            print("Produto encontrado!")
        else:
            print("Produto não encontrado!")

    elif opcao == 5:
        print("Quantidade de produtos:", len(carrinho))

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")