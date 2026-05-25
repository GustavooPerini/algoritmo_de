import random
import math

# Empresa produz produto A, B e C.
# Ela quer saber quantos produtos de cada tipo produzir para maximizar o lucro, respeitando limitações operacionais

# Lucro A: 30 moedas
# Lucro B: 50 moedas
# Lucro C: 40 moedas

# Produto A precisa de 2h de manufatura e 3 moedas.
# Produto B precisa de 4h de manufatura e 2 moedas.
# Produto C precisa de 3h de manufatura e 4 moedas

# Máximo de horas de máquina: 100h
# Máximo de recurso de matéria-prima: 90 moedas

###############################################################################################################################

# queremos maximizar a seguinte função: 30A + 50B + 40C
# respeitando as seguintes restrições:
# 2A + 4B + 3C <= 100
# 3A + 2B + 4C <= 90
# A + B + C >= 0


def verifica_restricao(sol):

    a, b, c = sol

    if min(sol) < 0:
        return False

    horas_maquina = 2*a + 4*b + 3*c
    materia_prima = 3*a + 2*b + 4*c
    
    return horas_maquina <= 100 and materia_prima <= 90

def funcao_avaliacao(sol):

    a, b, c = sol

    return 30*a + 50*b + 40*c

# Gera um vizinho aleatório
def gerar_vizinho(sol):

    # Vamos fazer um while que irá ocorrer até ser gerado um vizinho válido (que respeite as restrições).
    # Esse novo vizinho terá um de seus produtos aumentado ou diminuido em 1

    while True:
        nova = list(sol)

        produto = random.randint(0, 2)
        delta = random.choice([-1, 1])

        nova[produto] += delta

        if verifica_restricao(nova):
            return tuple(nova)

def simulated_anealing():

    atual = (10, 5, 8)
    melhor = atual

    T = 100 # Temperatura inicial
    T_min = 0.01 # Temperatura mínima
    alpha = 0.95 # Taxa de resfriamento

    while T > T_min:

        candidato = gerar_vizinho(atual)

        delta = funcao_avaliacao(candidato) - funcao_avaliacao(atual)

        if delta > 0:
            atual = candidato
        else:
            prop = math.exp(delta / T)

            if random.random() < prop:
                atual = candidato

        if funcao_avaliacao(atual) > funcao_avaliacao(melhor):
            melhor = atual

        T *= alpha
    
    return melhor
    
if __name__ == "__main__":

    solucao = simulated_anealing()

    print("Melhor plano de produção encontrado:")
    print(f"Produto A: {solucao[0]}")
    print(f"Produto B: {solucao[1]}")
    print(f"Produto C: {solucao[2]}")
    print(f"Lucro Máximo: R$ {funcao_avaliacao(solucao)}")