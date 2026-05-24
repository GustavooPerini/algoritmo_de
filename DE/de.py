import numpy as np
import matplotlib.pyplot as plt

N = 30
N_POPULACAO = 50
N_GERACOES = 800
LOW = -32
HIGH = 32

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

    if x[np.argmin(x)] < LOW or x[np.argmax(x)] > HIGH:
        punicao = 100

    return (term1 + term2 + 20 + np.e) * punicao


def gera_populacao():
    return np.random.uniform(low=LOW, high=HIGH, size=(N_POPULACAO, N))

def mutacao_cruzamento_selecao(populacao, fator=0.6, taxa_cross=0.7):
    nova_populacao = np.zeros((N_POPULACAO, N), float)
    for i in range(N_POPULACAO):

        # Mutacao
        first = populacao[np.random.randint(N_POPULACAO)]
        second = populacao[np.random.randint(N_POPULACAO)]
        third = populacao[np.random.randint(N_POPULACAO)]

        nova_populacao[i] = first + fator*(second - third)

        # Cruzamento
        for j in range(N):
            if np.random.random() > taxa_cross:
                nova_populacao[i][j] = populacao[i][j]

        # Selecao
        alvo = fitness(populacao[i])
        teste = fitness(nova_populacao[i])

        if alvo < teste:
            nova_populacao[i] = populacao[i]


    return nova_populacao

# Eixos do gráfico
fitness_por_geracao = np.zeros(shape=N_GERACOES, dtype=float)
geracoes = np.linspace(start=1, stop=N_GERACOES, num=N_GERACOES, dtype=int)

populacao = gera_populacao()
fitness_arr = []
melhor_idx = 0
for i in range(N_GERACOES):
    populacao = mutacao_cruzamento_selecao(populacao)

    # Necessário para plotar o gráfico posteriormente
    fitness_arr = np.array([fitness(ind) for ind in populacao])
    melhor_idx = np.argmin(fitness_arr)
    fitness_por_geracao[i] = fitness_arr[melhor_idx]

print("Melhor fitness encontrado: ", fitness_arr[melhor_idx])

# Plotando o gráfico
fig, ax = plt.subplots()

ax.plot(geracoes, fitness_por_geracao)

ax.set_xlabel("Geração")
ax.set_ylabel("Fitness")
ax.set_title("Algoritmo DE")
ax.legend(["Fitness"])

plt.show()