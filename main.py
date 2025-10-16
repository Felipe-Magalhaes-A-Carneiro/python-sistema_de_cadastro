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

iniciar = input("Digite 'y' para começar ou outro digito para sair do programa: ")

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

        # Condições de acesso ao menu:
        if opcao == '1':
            cadastro_emprestimos.cadastrar_emprestimos()

        # Condições de acesso aos registros já cadastrados:   
        elif opcao == '2':
            registro_emprestimos.registros_realizados()
            retornar_menu = input("\nDigite '0' para retornar ao MENU PRINCIPAL: ")
            if retornar_menu == '0':
                print("\nRetornando MENU PRINCIPAL...")
                return
            else:
                print("Apenas o digito '0'(zero) é permitido para sair e retornar ao MENU PRINCIPAL")
        
        # Condições para sair do programa: 
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            "Digite uma das opções válidas"

if iniciar == 'y':
    main()
else:
    print("Saindo do programa...")
    exit()