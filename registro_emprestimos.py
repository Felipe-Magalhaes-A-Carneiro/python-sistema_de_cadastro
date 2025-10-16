import cadastro_emprestimos

def registros_realizados():

    for cadastro in cadastro_emprestimos.emprestimo:
        print(f"""
    ____________________________________________________
    |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
    |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
    ----------------------------------------------------
        
    >>> REGISTROS REALIZADOS:
                  
        Usuário: {cadastro['usuario']}
        Livro: {cadastro['livro']}
        Avaliação: {cadastro['avaliacao']}
                  
    """)