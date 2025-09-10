# Passa a Bola - Simulador de Gestão do Futebol Feminino

# Dados iniciais (Pode ser substituído por um banco de dados real)
atletas = [
    {"nome": "Ana", "idade": 24, "posicao": "Meia", "clube": "Corinthians"},
    {"nome": "Bia", "idade": 22, "posicao": "Atacante", "clube": "Corinthians"},
    {"nome": "Carla", "idade": 27, "posicao": "Zagueira", "clube": "Flamengo"},
    {"nome": "Dani", "idade": 21, "posicao": "Goleira", "clube": "Flamengo"},
    {"nome": "Ela", "idade": 26, "posicao": "Lateral", "clube": "Palmeiras"},
    {"nome": "Fabi", "idade": 23, "posicao": "Volante", "clube": "Palmeiras"},
    {"nome": "Gabi", "idade": 28, "posicao": "Atacante", "clube": "Santos"},
    {"nome": "Hana", "idade": 20, "posicao": "Meia", "clube": "Santos"},
    {"nome": "Iara", "idade": 25, "posicao": "Ponta", "clube": "Corinthians"},
    {"nome": "Jo", "idade": 19, "posicao": "Meia", "clube": "Flamengo"},
    {"nome": "Karla", "idade": 30, "posicao": "Zagueira", "clube": "Palmeiras"},
]

clubes = [
    {"nome": "Corinthians", "cidade": "(exemplo)", "atletas": []},
    {"nome": "Flamengo", "cidade": "(exemplo)", "atletas": []},
    {"nome": "Palmeiras", "cidade": "(exemplo)", "atletas": []},
    {"nome": "Santos", "cidade": "(exemplo)", "atletas": []},
    {"nome": "Internacional", "cidade": "(exemplo)", "atletas": []},
    {"nome": "São Paulo", "cidade": "(exemplo)", "atletas": []},
]

partidas = [
    {"clubeA": "Corinthians", "clubeB": "Flamengo", "placar": "2 x 1"},
    {"clubeA": "Palmeiras", "clubeB": "Santos", "placar": "0 x 0"},
    {"clubeA": "Internacional", "clubeB": "São Paulo", "placar": "1 x 3"},
    {"clubeA": "Corinthians", "clubeB": "Palmeiras", "placar": "1 x 2"},
]

POSITIONS = [
    "Goleira",
    "Zagueira",
    "Lateral",
    "Volante",
    "Meia",
    "Atacante",
    "Ponta",
]

# Atualizar lista de atletas em cada clube ao iniciar o programa
for atleta in atletas:
    for clube in clubes:
        if atleta["clube"] == clube["nome"]:
            clube["atletas"].append(atleta["nome"])

# -------- Funções auxiliares --------
def read_non_empty(prompt):
    # Força o usuário a digitar algo que não seja vazio ou numérico
    value = input(prompt).strip()
    while not value or value.isnumeric():
        print("Entrada inválida. Digite novamente.")
        value = input(prompt).strip()
    return value

def read_positive_int(prompt):
    # Força o usuário a digitar um número positivo
    valor = input(prompt)
    while not valor.isnumeric() or int(valor) < 0:
        print("Entrada inválida. Digite um número positivo.")
        valor = input(prompt)
    return int(valor)

def select_option(options, prompt, allow_blank=False):
    # Força o usuário a escolher uma opção válida de uma lista
    for idx, opt in enumerate(options, start=1):
        print(f"{idx} - {opt}")
    if allow_blank:
        print("0 - Não especificar")

    choice = input(prompt).strip()
    
    while not choice.isnumeric() or int(choice) not in range(1, len(options)+1):
        print("Opção inválida. Tente novamente.")
        choice = input(prompt).strip()

    choice = int(choice)
    if allow_blank and choice == 0:
        return ""
    if 1 <= choice <= len(options):
        return options[choice-1]

# -------- Funcionalidades --------
def cadastrar_atleta():
    nome = read_non_empty("Digite o nome da atleta: ")
    idade = read_positive_int("Digite a idade da atleta: ")
    print("\nEscolha a posição da atleta:")
    posicao = select_option(POSITIONS, "Digite o número da posição: ")
    print("\nEscolha o clube da atleta:")
    nomes_clubes = [c["nome"] for c in clubes]
    clube = select_option(nomes_clubes, "Digite o número do clube: ")

    atleta = {"nome": nome, "idade": idade, "posicao": posicao, "clube": clube}
    atletas.append(atleta)
    # Adiciona atleta ao clube
    for c in clubes:
        if c["nome"] == clube:
            c["atletas"].append(nome)

    print(f"✅ Atleta {nome} cadastrada com sucesso!\n")

def cadastrar_clube():
    # Cadastrar novo clube
    nome = read_non_empty("Digite o nome do clube: ")
    cidade = read_non_empty("Digite a cidade do clube: ")
    clubes.append({"nome": nome, "cidade": cidade, "atletas": []})
    print(f"✅ Clube {nome} cadastrado com sucesso!\n")

def registrar_partida():
    # Registrar nova partida
    nomes_clubes = [c["nome"] for c in clubes]
    clubeA = select_option(nomes_clubes, "Escolha o Clube A: ")
    clubeB = select_option(nomes_clubes, "Escolha o Clube B: ")
    placarA = read_positive_int(f"Quantos gols o {clubeA} marcou? ")
    placarB = read_positive_int(f"Quantos gols o {clubeB} marcou? ")
    partidas.append({"clubeA": clubeA, "clubeB": clubeB, "placar": f"{placarA} x {placarB}"})
    print("✅ Partida registrada com sucesso!\n")

def listar_atletas():
    # Listar todas as atletas
    if not atletas:
        print("Nenhuma atleta cadastrada ainda.\n")
    else:
        print("\n📋 Lista de Atletas:")
        for a in atletas:
            print(f"- {a['nome']} ({a['posicao']}, {a['idade']} anos) - Clube: {a['clube']}")
        print("")

def listar_clubes():
    # Listar todos os clubes
    if not clubes:
        print("Nenhum clube cadastrado ainda.\n")
    else:
        print("\n📋 Lista de Clubes:")
        for c in clubes:
            print(f"- {c['nome']} ({c['cidade']}) - {len(c['atletas'])} atletas")
        print("")

def listar_partidas():
    # Listar todas as partidas
    if not partidas:
        print("Nenhuma partida registrada ainda.\n")
    else:
        print("\n📋 Lista de Partidas:")
        for p in partidas:
            print(f"- {p['clubeA']} vs {p['clubeB']} - Placar: {p['placar']}")
        print("")

# -------- Menu --------
def menu():
    while True:
        print("⚽ Bem-vindo ao sistema Passa a Bola ⚽")
        print("1 - Cadastrar Atleta")
        print("2 - Cadastrar Clube")
        print("3 - Registrar Partida")
        print("4 - Listar Atletas")
        print("5 - Listar Clubes")
        print("6 - Listar Partidas")
        print("7 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1": cadastrar_atleta()
        elif opcao == "2": cadastrar_clube()
        elif opcao == "3": registrar_partida()
        elif opcao == "4": listar_atletas()
        elif opcao == "5": listar_clubes()
        elif opcao == "6": listar_partidas()
        elif opcao == "7":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.\n")

menu()