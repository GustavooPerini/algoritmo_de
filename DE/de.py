import numpy as np

N = 30
N_POPULACAO = 100
N_GERACOES = 1000

def rastrigin_like(x):
    x = np.asarray(x)
    n = x.size

    term1 = -20 * np.exp(
        -0.2 * np.sqrt(np.sum(x**2) / n)
    )

    term2 = -np.exp(
        np.sum(np.cos(2 * np.pi * x)) / n
    )

    return term1 + term2 + 20 + np.e

def gera_individuo():
    return np.random.uniform(-32, 32, size=N)


def gera_populacao():
    populacao = np.zeros((N_POPULACAO, N), float)

    for i in range(N_POPULACAO):
        populacao[i] = gera_individuo()

    return populacao

def mutacao(populacao, fator=0.6):
    nova_populacao = np.zeros((N_POPULACAO, N), float)
    for i in range(N_POPULACAO):
        first = populacao[np.random.randint(N_POPULACAO)]
        second = populacao[np.random.randint(N_POPULACAO)]
        third = populacao[np.random.randint(N_POPULACAO)]

        nova_populacao[i] = first + fator*(second - third)
    return nova_populacao

def crossover(populacao_inicial, populacao_mutada, taxa_cross=0.7):
    nova_populacao = np.zeros((N_POPULACAO, N), float)
    for i in range(N_POPULACAO):
        for j in range(N):
            if np.random.random() <= taxa_cross:
                nova_populacao[i][j] = populacao_mutada[i][j]
            else:
                nova_populacao[i][j] = populacao_inicial[i][j]
    return nova_populacao

def selecao(populacao_inicial, populacao_cross):
    nova_populacao = np.zeros((N_POPULACAO, N), float)
    for i in range(N_POPULACAO):
        alvo = populacao_inicial[i]
        teste = populacao_cross[i]

        fit_alvo = rastrigin_like(alvo)
        fit_teste = rastrigin_like(teste)

        if np.any(teste < -32) or np.any(teste > 32):
            fit_teste += 100000
        if np.any(alvo < -32) or np.any(alvo > 32):
            fit_alvo += 100000

        if fit_teste <= fit_alvo:
            nova_populacao[i] = fit_teste
        else:
            nova_populacao[i] = fit_alvo
    return nova_populacao

populacao = gera_populacao()
for i in range(N_GERACOES):
    populacao_mutada = mutacao(populacao)
    populacao_cross = crossover(populacao, populacao_mutada)
    populacao = selecao(populacao, populacao_cross)

melhor_individuo = populacao[0]
melhor_fitness = rastrigin_like(melhor_individuo)

for ind in populacao:
    fit = rastrigin_like(ind)
    if fit < melhor_fitness:
        melhor_fitness = fit
        melhor_individuo = ind

print("Melhor fitness encontrado: ", melhor_fitness)