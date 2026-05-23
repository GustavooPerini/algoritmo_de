import numpy as np

N = 30
POPULACAO = 100
LOW = -32
HIGH = 32

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

def gera_populacao():
    return np.random.uniform(low=LOW, high=HIGH, size=(POPULACAO, N))