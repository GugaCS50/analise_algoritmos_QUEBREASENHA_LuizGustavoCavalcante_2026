import random
from src.config import charset, password_size

def gerar_individuo():
    return ''.join(
        random.choice(charset)
        for _ in range(password_size)
    )

def crossover(pai1, pai2):

    ponto = random.randint(
        1, password_size - 1
    )
    filho = (
        pai1[:ponto]+pai2[ponto:]
    )
    return filho

def mutacao(individuo, taxa=0.1):
    individuo = list(individuo)
    for i in range(password_size):
        if random.random() < taxa:

            individuo[i] = random.choice(charset)

    return ''.join(individuo)

def solve_genetic(
        oracle,
        tamanho_populacao=200,
        geracoes=10000,
        taxa_mutacao=0.1
):
    
    populacao = [
        gerar_individuo()
        for _ in range(tamanho_populacao)
    ]

    for geracao in range(geracoes):
        fitness_score = []
        for individuo in populacao:

            fitness = oracle.get_fitness(individuo)

            fitness_score.append(
                (fitness, individuo)
            )

        fitness_score.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        best_fitness = fitness_score[0][0]
        best_individuo = fitness_score[0][1]

        if best_fitness == password_size:

            return best_individuo
        
        sobreviventes = [
            individuo
            for _, individuo
            in fitness_score[:50]
        ]

        new_populacao = sobreviventes.copy()

        while(
            len(new_populacao)<tamanho_populacao
        ):
            pai1 = random.choice(sobreviventes)
            pai2 = random.choice(sobreviventes)

            filho = crossover(pai1, pai2)
            filho = mutacao(filho, taxa_mutacao)

            new_populacao.append(filho)

        populacao = new_populacao

    return None