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
            Digite o número de uma das opções abaixo: 
              
        1 - Iniciar cadastramentos;
        
        0 - Voltar para o Menu Principal.
        
        """)

        opcao = input("Digite a sua escolha: ")

        if opcao == '1':
            print("""
        ____________________________________________________
        |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
        |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
        ----------------------------------------------------
        
        >>> CADASTRAMENTO DE LIVROS EMPRESTADOS
                  
            ATENÇÃO: O cadastramento ocorre de forma continua, para parar o processo, digite ' 0 ' (zero), em usuário.
                  
        """)
            nome_usuario = input("Digite o nome do USUÁRIO(aluno): ").title()
            if nome_usuario == '0':
                print("\n Retornando para o MENU PRINCIPAL...")
                return
            else:
                nome_livro = input("\nDigite o nome do LIVRO: ").title()
                comentario = input(f"\nDigite a AVALIAÇÃO do aluno sobre o livro {nome_livro}: ")
            
                cadastrar = {'usuario' : nome_usuario, 'livro': nome_livro, 'avaliacao' : comentario }
                emprestimo.append(cadastrar)

                print("\n Cadastro realizado com SUCESSO...\n")

                
            registro_emprestimos.registros_realizados()
