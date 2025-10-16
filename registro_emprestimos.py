import cadastro_emprestimos

def registros_realizados():
    print(f"""
    ____________________________________________________
    |=== BIBLIOTECA SENAI Morgan Figueiredo - Mooca ===|
    |======= SISTEMA DE CADASTRAMENTO DE LIVROS =======|
    ----------------------------------------------------
    
    >>> REGISTROS REALIZADOS: """)

    if cadastro_emprestimos.emprestimo != []:
        # retorna o registro finalizado em que cada vez ele for feito:        
        for cadastro in cadastro_emprestimos.emprestimo:
            print(f"""
        Usuário: {cadastro['usuario']}
        Livro: {cadastro['livro']}
        Avaliação: {cadastro['avaliacao']}
        --------------------------------------------         
        """)
    else:
        print("\n*** ATENÇÃO: Ainda não houveram registros no sistema...***")
        