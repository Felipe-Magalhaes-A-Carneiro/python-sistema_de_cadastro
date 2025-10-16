import registro_emprestimos

emprestimo = []

def cadastrar_emprestimos():
    while True:
        print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------
        
        >>> CADASTRAMENTO DE LIVROS EMPRESTADOS
            ATENÇÃO: O cadastramento ocorre de forma continua, para parar o processo, digite ' 0 ' (zero), em usuário.
        
        """)
        nome_usuario = input(">>> Digite o nome do USUÁRIO(aluno): ").title()
            # condição para sair da função atual
        if nome_usuario == '0':
            print("\n Retornando para o MENU PRINCIPAL...")
            break
        else:
            nome_livro = input("\n>>> Digite o nome do LIVRO: ").title()
            comentario = input(f"\n>>> Digite a AVALIAÇÃO do aluno sobre o livro '{nome_livro}': ")
            
            cadastrar = {'usuario' : nome_usuario, 'livro': nome_livro, 'avaliacao' : comentario }
            emprestimo.append(cadastrar)

            print("\nCadastro realizado com SUCESSO...\n")

        registro_emprestimos.registros_realizados()

