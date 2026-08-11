Sistema de Gerenciamento de Biblioteca
Descrição

Este projeto é um sistema simples de gerenciamento de biblioteca desenvolvido em Python.

O programa permite cadastrar livros e controlar se eles estão disponíveis ou emprestados. Também é possível pesquisar, listar e organizar os livros cadastrados.

Os dados dos livros são salvos no arquivo livros.csv, para que não sejam perdidos quando o programa for fechado.

Como executar

Para executar o programa, é necessário ter o Python instalado.

Abra o terminal na pasta do projeto e execute:

python main.py

Depois disso, o menu principal será exibido no terminal. Basta escolher uma das opções disponíveis.

Principais funcionalidades
Cadastrar livros
Registrar empréstimo de livros
Registrar devolução de livros
Listar todos os livros cadastrados
Buscar livros por título ou autor
Ordenar livros por título, autor ou ano de publicação
Salvar os dados dos livros em um arquivo CSV
Requisitos técnicos aplicados
Menu com if/elif/else: usado no menu principal para controlar as opções escolhidas pelo usuário.
Estrutura while: usada para manter o menu funcionando até o usuário escolher a opção de sair.
Funções próprias: o programa possui funções como cadastrar_livro(), emprestar_livro(), devolver_livro(), listar_livros(), buscar_livro() e ordenar_livros().
Lista de dicionários: os livros são armazenados em uma lista, sendo cada livro representado por um dicionário com título, autor, ano, ISBN e status.
Persistência em arquivo: os dados são salvos no arquivo livros.csv e carregados novamente quando o programa é iniciado.
Leitura e escrita de arquivo: o módulo csv, que faz parte da biblioteca padrão do Python, é utilizado para ler e salvar os dados.