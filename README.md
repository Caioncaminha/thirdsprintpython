# Computational Thinking with Python - Sprint 3 (Passa a Bola)

## 🧠 1. Descrição

Simulador CLI em **Python** que gerencia um cadastro simples de **atletas**, **clubes** e **partidas** usando **listas** e **dicionários**. Feito para demonstrar lógica de dados (chaves/valores), validação básica de entrada e operações CRUD (Create, Read, Update, Delete) mínimas em memória.

---

## 🛠️ 2. Tecnologias

* Linguagem: **Python** (sem dependências externas)
* Persistência atual: **in-memory** (listas/dicionários)

---

## 🎲 3. Dados iniciais (modelo)

Usamos listas de dicionários:

* `atletas` — cada item: `{"nome","idade","posicao","clube"}`
* `clubes` — cada item: `{"nome","cidade","atletas"}`
* `partidas` — cada item: `{"clubeA","clubeB","placar"}`
* `POSITIONS` — lista fixa de posições permitidas

No início, o script já sincroniza os nomes das atletas em `clubes[].atletas`.

---

## 🧩 4. Estrutura do código (funções principais)

### Funções de leitura/validação
  * `read_non_empty(prompt)` — força texto não vazio/não numérico
  * `read_positive_int(prompt)` — força inteiro >= 0
  * `select_option(options, prompt, allow_blank=False)` — escolha de lista com validação

### Funcionalidades CRUD
  * `cadastrar_atleta()` — valida entradas, escolhe posição e clube, atualiza listas
  * `cadastrar_clube()` — cria novo clube
  * `registrar_partida()` — registra placar e armazena partida
  * `listar_atletas()`, `listar_clubes()`, `listar_partidas()` — exibe dados

### Interface
  * `menu()` — loop principal com opções numeradas (1...7)

---

## ✅ 5. Funcionalidades implementadas

* Cadastro de atleta com validação de posição e vínculo ao clube
* Cadastro de clube com cidade
* Registro de partidas com entrada de placar numérico
* Listagem de atletas, clubes (com contagem de atletas) e partidas
* Proteções básicas de entrada (não permite strings vazias, força números positivos)

---

## ▶️ 6. Como rodar

1. Salva o arquivo (ex.: `passabola.py`) com o código que você tem.
2. No terminal:

```bash
python main.py
```

3. Segue o menu e digita as opções (1 a 7).

Nenhum pacote adicional é necessário.

---

## 👥 Integrantes A-Z

- Caio Nascimento Caminha
- Gabriel Alexandre Fukushima Sakura
- Gabriel Oliveira Amaral
- Lucas Henrique Viana Estevam Sena
- Rafael Tavares Santos

---

## 📜 Licença

Projeto acadêmico. Uso livre para fins educacionais.