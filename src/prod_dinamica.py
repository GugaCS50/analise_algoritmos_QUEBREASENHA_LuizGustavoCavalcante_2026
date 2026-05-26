from src.config import charset, password_size

def solve_prefix(
        oracle, prefix, memo
):
    if prefix in memo:
        return memo[prefix]
    
    valido = oracle.check_partial(
        prefix,0
    )
    memo[prefix] = valido
    
    return valido

def solve_prog_dinamica(oracle):

    senha = ''
    memo = {}

    for pos in range(password_size):

        for char in charset:
            tentativa = senha + char

            if solve_prefix(
                oracle, tentativa, memo
            ):
                senha += char

                break
    
    return senha