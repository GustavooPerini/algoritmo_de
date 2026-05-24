import numpy as np
import matplotlib.pyplot as plt

POPULACAO = 150
DIMENSOES = 30
W = 0.6
C1 = 2.05
C2 = 2.05
N_GERACAO = 2200
LOW = -32
HIGH = 32


# Indivíduo == partícula
# Cada indivíduo da população possui 30 dimensões.
# Cada partícula possui:
# Uma posição xi, onde i referencia a partícula. Cada posição possui 30 dimensões por x1, x2, ..., x30
# Uma velocidade vi, onde i referencia a partícula. Cada velocidade possui 30 dimensões, ou seja, v1, v2, ..., v30
# Melhor posição individual pbest_i, onde i referencia a partícula
# Melhor posição global gbest


def gera_populacao():
    return np.random.uniform(low=LOW, high=HIGH, size=(POPULACAO, DIMENSOES))

def gera_velocidades():
    return np.random.uniform(low=-1, high=1, size=(POPULACAO, DIMENSOES))

def fitness(x):

    punicao = 1

    x = np.asarray(x)
    n = x.size

    term1 = -20 * np.exp(
        -0.2 * np.sqrt(np.sum(x**2) / n)
    )

    term2 = -np.exp(
        np.sum(np.cos(2 * np.pi * x)) / n
    )

    if x[np.argmin(x)] < -32 or x[np.argmax(x)] > 32:
        punicao = 100

    return (term1 + term2 + 20 + np.e) * punicao

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

fitness_por_geracao = np.zeros(shape=N_GERACAO, dtype=float)
geracoes = np.linspace(start=1, stop=N_GERACAO, num=N_GERACAO)
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
    
    fitness_por_geracao[i] = g_best_fitness

print(f"Melhor fitness: {g_best_fitness}")

# Plotando o gráfico
fig, ax = plt.subplots()

ax.plot(geracoes, fitness_por_geracao)
ax.set_xlabel("Gerações")
ax.set_ylabel("Fitness")
ax.set_title("Algoritmo PSO")
ax.legend(["Fitness"])

plt.show()