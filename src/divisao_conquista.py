from itertools import product
from src.config import charset

def find_block(
        oracle, size_block, posicao
):
    for combination in product(
        charset, repeat=size_block
    ):
        tentativa = ''.join(combination)

        if oracle.check_partial(
            tentativa, posicao
        ):
            return tentativa
        
def resolve_div_conquista(oracle):
    metade = 4

    part1 = find_block(
        oracle, metade, 0
    )

    part2 = find_block(
        oracle, metade, 4
    )

    return part1+part2