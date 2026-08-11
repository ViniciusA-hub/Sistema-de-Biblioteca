import csv

ARQUIVO = "livros.csv"


def carregar_livros():
    livros = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)

    except FileNotFoundError:
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            campos = ["titulo", "autor", "ano", "isbn", "status"]
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()

    return livros


def salvar_livros(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)

    return True


def cadastrar_livro(livros):
    print("\n--- CADASTRO DE LIVRO ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("Código/ISBN: ").strip()

    if titulo == "" or autor == "" or ano == "" or isbn == "":
        print("Todos os campos devem ser preenchidos.")
        return False

    try:
        ano = int(ano)
    except ValueError:
        print("O ano deve ser um número.")
        return False

    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro com esse código/ISBN.")
            return False

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")
    return True
def emprestar_livro(livros):
    print("\n--- EMPRÉSTIMO DE LIVRO ---")
    isbn = input("Código/ISBN do livro: ").strip()

    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                print(f"Livro '{livro['titulo']}' emprestado com sucesso!")
                return True
            else:
                print("O livro já está emprestado.")
                return False

    print("Livro não encontrado.")
    return False
def devolver_livro(livros):
    print("\n--- DEVOLUÇÃO DE LIVRO ---")
    isbn = input("Código/ISBN do livro: ").strip()

    for livro in livros:
        if livro["isbn"] == isbn:
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                print(f"Livro '{livro['titulo']}' devolvido com sucesso!")
                return True
            else:
                print("O livro não está emprestado.")
                return False

    print("Livro não encontrado.")
    return False
def listar_livros(livros):
    print("\n--- LISTA DE LIVROS ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"Código/ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("------------------------")
def buscar_livro(livros):
    print("\n--- BUSCAR LIVRO ---")
    isbn = input("Código/ISBN do livro: ").strip()

    for livro in livros:
        if livro["isbn"] == isbn:
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Código/ISBN: {livro['isbn']}")
            print(f"Status: {livro['status']}")
            return

    print("Livro não encontrado.")
def ordenar_livros(livros):
    print("\n--- ORDENAR LIVROS ---")
print("1. Ordenar por título")
print("2. Ordenar por autor")
print("3. Ordenar por ano")
opcao = input("Escolha uma opção: ").strip()

if opcao == "1":
        livros.sort(key=lambda x: x["titulo"])
        print("Livros ordenados por título.")
elif opcao == "2":
        livros.sort(key=lambda x: x["autor"])
        print("Livros ordenados por autor.")
elif opcao == "3":
        livros.sort(key=lambda x: x["ano"])
        print("Livros ordenados por ano.")
else:
        print("Opção inválida..")
def mostrar_menu():
    print("\n--- MENU ---")
    print("1. Cadastrar livro")
    print("2. Emprestar livro")
    print("3. Devolver livro")
    print("4. Listar livros")
    print("5. Buscar livro")
    print("6. Ordenar livros")
    print("7. Sair")
    livros = carregar_livros()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        if cadastrar_livro(livros):
            salvar_livros(livros)
    elif opcao == "2":
        if emprestar_livro(livros):
            salvar_livros(livros)
    elif opcao == "3":
        if devolver_livro(livros):
            salvar_livros(livros)
    elif opcao == "4":
        listar_livros(livros)
    elif opcao == "5":
        buscar_livro(livros)
    elif opcao == "6":
        ordenar_livros(livros)
        salvar_livros(livros)
    elif opcao == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")