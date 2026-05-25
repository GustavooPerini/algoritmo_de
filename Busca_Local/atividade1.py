import random
import math

# A empresa quer maximizar o retorno esperado da campanha.
# Nisso, ela quer saber o quanto investir em cada canal.

# Retorno bruto de cada canal:
# Google Ads: 50 * x1 - 1.2 * (x1**2)
# Instagram Ads: 45 * x2 - 1.0 * (x2**2)
# Linkedin Ads: 40 * x3 - 0.8 * (x3**2)
# YouTube Ads: 55 * x4 - 1.5 * (x4**2)

# Restrições:
# x1 + x2 + x3 + x4 <= 50
# x3 + x4 <= 25
# 2 * x1 + x2 + 3 *x3 + 2 * x4 <= 80
# x1 + x2 + x3 + x4 >= 0


def funcao_objetivo(sol):

    x1, x2, x3, x4 = sol

    return ((50 * x1) - (1.2 * (x1**2))) + ((45 * x2) - (1.0 * (x2**2))) + ((40 * x3) - (0.8 * (x3**2))) + ((55 * x4) - (1.5 * (x4**2)))

def verifica_restricoes(sol):

    x1, x2, x3, x4 = sol

    if min(sol) < 0:
        return False
    
    investimento_max = x1 + x2 + x3 + x4
    canais_premium = x3 + x4
    capacidade_operacional = (2 * x1) + x2 + (3 *x3) + (2 * x4)

    return investimento_max <= 50 and canais_premium <= 25 and capacidade_operacional <= 80

def gera_vizinho(sol):

    while True:

        nova = list(sol)

        i = random.randint(0, 3)
        delta = random.choice([-1, 1])

        nova[i] += delta

        if verifica_restricoes(nova):
            return tuple(nova)
        
def simulated_annealing():

    atual = (0, 0, 0)
    melhor = atual


    return melhor
