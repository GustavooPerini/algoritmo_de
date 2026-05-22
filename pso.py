import numpy as np

POPULACAO = 100
DIMENSOES = 30
W = 0.6
C1 = 2.05
C2 = 2.05
N_GERACAO = 1900


# Indivíduo == partícula
# Cada indivíduo da população possui 30 dimensões.
# Cada partícula possui:
# Uma posição xi, onde i referencia a partícula. Cada posição possui 30 dimensões por x1, x2, ..., x30
# Uma velocidade vi, onde i referencia a partícula. Cada velocidade possui 30 dimensões, ou seja, v1, v2, ..., v30
# Melhor posição individual pbest_i, onde i referencia a partícula
# Melhor posição global gbest


def gera_populacao():
    return np.random.uniform(-100, 100, (POPULACAO, DIMENSOES))

def gera_velocidades():
    return np.random.uniform(-1, 1, (POPULACAO, DIMENSOES))


def fitness(x):
    penalidade = 1
    if x[np.argmin(x)] < -100 or x[np.argmax(x)] > 100:
        penalidade = 100
    return np.sum(x**2) * penalidade

def atualiza_velocidade(p_best, g_best, x, v):
    r1 = np.random.random(x.shape)
    r2 = np.random.random(x.shape)
    return (W * v) + (C1 * r1 * (p_best - x)) + (C2 * r2 * (g_best - x))

def atualiza_posicao(x, v):
    return x + v

# Inicialização
populacao = gera_populacao()
velocidade = gera_velocidades()
fitness_arr = np.array([fitness(x) for x in populacao])

# pbest
p_best = np.copy(populacao)
p_best_fitness = np.copy(fitness_arr)

# gbest
g_best_idx = np.argmin(fitness_arr)
g_best = np.copy(populacao[g_best_idx])
g_best_fitness = fitness_arr[g_best_idx]


for i in range(N_GERACAO):
    
    velocidade = atualiza_velocidade(p_best, g_best, populacao, velocidade)
    populacao = atualiza_posicao(populacao, velocidade)
    
    novo_fitness = np.array([fitness(x) for x in populacao])

    for j in range(POPULACAO):

        if novo_fitness[j] < p_best_fitness[j]:
            p_best[j] = np.copy(populacao[j])
            p_best_fitness[j] = novo_fitness[j]

            if novo_fitness[j] < g_best_fitness:
                g_best = np.copy(populacao[j])
                g_best_fitness = novo_fitness[j]

print(f"Melhor fitness: {g_best_fitness}")
print(f"Melhor posição: {g_best}")