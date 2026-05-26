from itertools import product

from src.config import (
    CHARSET,
    PASSWORD_SIZE
)


def resolve_forca_bruta(oracle):

    for combination in product(
        CHARSET,
        repeat=PASSWORD_SIZE
    ):

        attempt = ''.join(combination)

        if oracle.check_full(attempt):

            return attempt