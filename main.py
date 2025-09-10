# Passa a Bola - Simulador Básico de Gestão do Futebol Feminino

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
    value = input(prompt).strip()
    while not value or value.isspace():
        print("Entrada inválida. Digite novamente.")
        value = input(prompt).strip()
    return value

def read_positive_int(prompt):
    while True:
        valor = input(prompt)
        if valor.isnumeric() and int(valor) > 0:
            return int(valor)
        print("Entrada inválida. Digite um número positivo.")

def read_non_negative_int(prompt):
    while True:
        valor = input(prompt)
        if valor.isnumeric() and int(valor) >= 0:
            return int(valor)
        print("Entrada inválida. Digite um número válido.")

def select_option(options, prompt, allow_blank=False):
    for idx, opt in enumerate(options, start=1):
        print(f"{idx} - {opt}")
    if allow_blank:
        print("0 - Não especificar")

    while True:
        choice = input(prompt).strip()
        if choice.isnumeric():
            n = int(choice)
            if allow_blank and n == 0:
                return ""
            if 1 <= n <= len(options):
                return options[n-1]
        print("Opção inválida. Tente novamente.")

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
    # adiciona atleta ao clube
    for c in clubes:
        if c["nome"] == clube:
            c["atletas"].append(nome)

    print(f"✅ Atleta {nome} cadastrada com sucesso!\n")

def cadastrar_clube():
    nome = read_non_empty("Digite o nome do clube: ")
    cidade = read_non_empty("Digite a cidade do clube: ")
    clubes.append({"nome": nome, "cidade": cidade, "atletas": []})
    print(f"✅ Clube {nome} cadastrado com sucesso!\n")

def registrar_partida():
    clubeA = read_non_empty("Digite o nome do Clube A: ")
    clubeB = read_non_empty("Digite o nome do Clube B: ")
    placarA = read_non_negative_int(f"Quantos gols o {clubeA} marcou? ")
    placarB = read_non_negative_int(f"Quantos gols o {clubeB} marcou? ")
    partidas.append({"clubeA": clubeA, "clubeB": clubeB, "placar": f"{placarA} x {placarB}"})
    print("✅ Partida registrada com sucesso!\n")

def listar_atletas():
    if not atletas:
        print("Nenhuma atleta cadastrada ainda.\n")
    else:
        print("\n📋 Lista de Atletas:")
        for a in atletas:
            print(f"- {a['nome']} ({a['posicao']}, {a['idade']} anos) - Clube: {a['clube']}")
        print("")

def listar_clubes():
    if not clubes:
        print("Nenhum clube cadastrado ainda.\n")
    else:
        print("\n📋 Lista de Clubes:")
        for c in clubes:
            print(f"- {c['nome']} ({c['cidade']}) - {len(c['atletas'])} atletas")
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
        print("6 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        while not opcao.isnumeric() or int(opcao) not in range(1, 7):
            print("❌ Opção inválida, tente novamente.\n")
            opcao = input("Escolha uma opção: ").strip()
        if opcao == "1": cadastrar_atleta()
        elif opcao == "2": cadastrar_clube()
        elif opcao == "3": registrar_partida()
        elif opcao == "4": listar_atletas()
        elif opcao == "5": listar_clubes()
        elif opcao == "6":
            print("👋 Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente.\n")

# Executar o programa
if __name__ == "__main__":
    menu()