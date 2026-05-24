import numpy as np
import matplotlib.pyplot as plt

N = 30
N_POPULACAO = 30
N_GERACOES = 20
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

def selecao(populacao, fitness_arr):
    nova_populacao = np.zeros(shape=(N_POPULACAO, N), dtype=float)

    for i in range(N_POPULACAO):
        ind1_idx = np.random.randint(low=0, high=N_POPULACAO)
        ind2_idx = np.random.randint(low=0, high=N_POPULACAO)

        if fitness_arr[ind1_idx] < fitness_arr[ind2_idx]:
            nova_populacao[i] = populacao[ind1_idx]
        else:
            nova_populacao[i] = populacao[ind2_idx]

    return nova_populacao

def cruzamento(populacao, taxa_cruzamento=0.7):
    nova_populacao = np.zeros(shape=(N_POPULACAO, N), dtype=float)

    for i in range(N_POPULACAO // 2):
        pai1_idx = np.random.randint(low=0, high=N_POPULACAO)
        pai2_idx = np.random.randint(low=0, high=N_POPULACAO)

        pai1 = populacao[pai1_idx]
        pai2 = populacao[pai2_idx]

        if np.random.random() <= taxa_cruzamento:
            beta = np.random.normal(loc=0, scale=1)
            pai1 = (beta * pai1) + ((1 - beta) * pai2)
            pai2 = ((1 - beta) * pai1) + (beta * pai2)
        
        nova_populacao[i*2] = pai1
        nova_populacao[(i*2) + 1] = pai2
    
    return nova_populacao

def mutacao(populacao, taxa_mutacao=0.1):
    
    for i in range(N_POPULACAO):
        if np.random.random() <= taxa_mutacao:
            alfa = np.random.normal(loc=0, scale=1)
            populacao[i] = populacao[i] * alfa

    
melhor_ftiness_por_geracao = np.zeros(shape=N_GERACOES, dtype=float)
geracoes = np.linspace(start=1, stop=N_GERACOES, num=N_GERACOES, dtype=int)

populacao = gera_populacao()
for i in range(N_GERACOES):

    # Aplicando a fitness em todos os indivíduos
    fitness_arr = np.array([fitness(ind) for ind in populacao])

    # Pegando o indivíduo com o menor fitness dessa população
    melhor_idx = np.argmin(fitness_arr)
    melhor_indv = np.copy(populacao[melhor_idx])

    # Pegando a melhor fitness dessa geração para plotar o gráfico posteriormente
    melhor_ftiness_por_geracao[i] = fitness_arr[melhor_idx]

    populacao = selecao(populacao, fitness_arr)
    populacao = cruzamento(populacao)
    mutacao(populacao)

    # Aplicando o elitismo
    populacao[0] = melhor_indv

fitness_final = np.array([fitness(ind) for ind in populacao])
melhor_idx = np.argmin(fitness_final)

print("Melhor fitness encontrado: ", fitness_final[melhor_idx])

# Plotando o gráfico
fig, ax = plt.subplots()

ax.plot(geracoes, melhor_ftiness_por_geracao)

ax.set_xlabel("Geração")
ax.set_ylabel("Fitness")
ax.set_title("Algoritmo GA")
ax.legend(["Fitness"])

plt.show()