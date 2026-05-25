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

def gerar_vizinhos(sol):

    vizinhos = []

    for i in range(len(sol)):
        for delta in [-1, 1]:
            nova = list(sol)
            nova[i] += delta
            if verifica_restricao(nova):
                vizinhos.append(tuple(nova))

    return vizinhos

def hill_climbing():

    atual = (10, 5, 8)

    while True:

        vizinhos = gerar_vizinhos(atual)

        if not vizinhos:
            break

        melhor = max(vizinhos, key=funcao_avaliacao)

        if funcao_avaliacao(melhor) <= funcao_avaliacao(atual):
            break

        atual = melhor

    return atual

if __name__ == "__main__":

    solucao = hill_climbing()

    print("Melhor plano de produção encontrado:")
    print(f"Produto A: {solucao[0]}")
    print(f"Produto B: {solucao[1]}")
    print(f"Produto C: {solucao[2]}")
    print(f"Lucro Máximo: R$ {funcao_avaliacao(solucao)}")