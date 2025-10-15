# "Sistema de Cadastramento de Livros emprestados - DESAFIO - Fundamentos básicos Python - Biblioteca"

import cadastro_emprestimos
import registro_emprestimos

print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------

Seja bem-vindo(a).
Cadastre um aluno(a)(usuario), o livro e a avaliação dele.

ATENÇÃO: Siga as instruções em cada menu que disponibilizarmos.
""")

iniciar = input("Digite 'y' para começar: ")

def main():
    while True:

        print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------
        
        >>> MENU PRINCIPAL
            Digite o número de uma das opções abaixo:
              
        1- Cadastramento de empréstimos;
        2- Registro de empréstimos já cadastrados;
        
        3- Sair do sistema.

        """)

        opcao = input("Digite a sua escolha: ")

        # condições de acesso ao menu:
        if opcao == '1':
            print("\n1- Cadastramento de empréstimos")
        elif opcao == '3':
            break
        else:
            "Digite uma das opções válidas"

if iniciar == 'y':
    main()
else:
    print("Saindo do sistema...")
    exit()