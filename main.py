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
