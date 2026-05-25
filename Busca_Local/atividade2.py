import numpy as np
import matplotlib.pyplot as plt

LOW = -1
HIGH = 2

def funcao_avaliacao(x):
    return (x*np.sin(10*np.pi*x)) + 1

def gera_vizinho(atual):
    perturbacao = np.random.uniform(-0.5, 0.5)
    vizinho = atual + perturbacao
    return np.clip(vizinho, LOW, HIGH)

def simulated_annealing():

    atual = np.random.uniform(low=LOW, high=HIGH)
    melhor = atual

    T = 100 # Temperatura
    T_min = 0.01 # Temperatura mínima
    alpha = 0.95

    while T > T_min:
        
        candidato = gera_vizinho(atual)

        delta = funcao_avaliacao(candidato) - funcao_avaliacao(atual)

        if delta > 0:
            atual = candidato
        else:
            prob = np.exp(delta / T)
            if np.random.random() < prob:
                atual = candidato
        
        if funcao_avaliacao(atual) > funcao_avaliacao(melhor):
            melhor = atual
        
        T *= alpha

    return melhor

if __name__ == "__main__":

    solucao = simulated_annealing()

    print(f"O máximo global é: {funcao_avaliacao(solucao)}")

    x = np.linspace(start=LOW, stop=HIGH, num=100)

    fig, ax = plt.subplots()

    ax.plot(x, funcao_avaliacao(x))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Função objetivo")

    plt.show()