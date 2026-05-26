import argparse
import time
from src.oracle import Oracle
from src.forca_bruta import resolve_forca_bruta
from src.divisao_conquista import resolve_div_conquista
from src.prod_dinamica import solve_prog_dinamica
from src.genetico import solve_genetic


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--algo')
    parser.add_argument('--mode')
    parser.add_argument('--path', default=None)

    args = parser.parse_args()

    if args.mode == 'file':

        oracle = Oracle(
            mode='file',
            path=args.path
        )
    else:

        oracle = Oracle(mode='random')

    start = time.time()

    if args.algo == 'brute':
        password = resolve_forca_bruta(oracle)

    elif args.algo == 'divide':

        password = resolve_div_conquista(oracle)

    elif args.algo == 'dynamic':

        password = solve_prog_dinamica(oracle)


    elif args.algo == 'genetic':

        password = solve_genetic(oracle)
    

    else:
        print('Algoritmo inválido.')
        return

    end = time.time()
    elapsed = end - start

    print('Senha carregada: {password}')
    print(f'Tempo: {elapsed:.5f}s')
    print(f'Hits: {oracle.get_hits()}')

if __name__ == '__main__':
    main()