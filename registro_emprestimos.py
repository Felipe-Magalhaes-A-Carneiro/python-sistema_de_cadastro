import cadastro_emprestimos

def registros_realizados():
    print(f"""
    ____________________________________________________
    |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
    |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
    ----------------------------------------------------
    
    >>> REGISTROS REALIZADOS:
    """)
            
    for cadastro in cadastro_emprestimos.emprestimo:
        print(f"""
    Usuário: {cadastro['usuario']}
    Livro: {cadastro['livro']}
    Avaliação: {cadastro['avaliacao']}
    --------------------------------------------         
    """)