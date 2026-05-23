import numpy as np

NUM_INDIVIDUOS = 100
NUM_GENES = 10

class Gene:
    def __init__(self, comprimento, vazao_acc, tubo):
        self.comprimento = comprimento
        self.vazao_acc = vazao_acc
        self.tubo = tubo

class Tubo:
    def __init__(self, diametro, custo):
        self.diametro = diametro/1000 # convertendo de mm para m
        self.custo = custo

class Individuo:
    def __init__(self, genes):
        self.genes = genes

def printa_individuo(individuo):
    for i in range(NUM_GENES):
        print(f"trecho {i}")
        print("comprimento: ", individuo.genes[i].comprimento)
        print("vazao acumulada: ", individuo.genes[i].vazao_acc)
        print("diametro do tubo: ", individuo.genes[i].tubo.diametro)
        print("custo por m do tubo: ", individuo.genes[i].tubo.custo)

def capacidade_de_vazao(tubo):
    n = 0.013
    a = (np.pi * (tubo.diametro**2)) / 4
    rh = tubo.diametro / 4
    s = 0.005

    return 1/n * a * (rh**(2/3)) * np.sqrt(s)

def calcula_custo(individuo):
    custo_total = 0
    punicao = 0
    
    for i in range(NUM_GENES):
        custo_total += individuo.genes[i].comprimento * individuo.genes[i].tubo.custo
        if individuo.genes[i].vazao_acc > 0.75 * capacidade_de_vazao(individuo.genes[i].tubo):
            punicao += 1000
    
    return custo_total + punicao

def selecao(populacao):
    nova_populacao = []
    for i in range(5):
        idx_1 = np.random.randint(low=0, high=5)
        idx_2 = np.random.randint(low=0, high=5)

        if calcula_custo(populacao[idx_1]) < calcula_custo(populacao[idx_2]):
            nova_populacao.append(populacao[idx_1])
        else:
            nova_populacao.append(populacao[idx_2])
    return nova_populacao

# Trechos
comprimentos = [20, 54, 98, 120, 34, 12, 88, 122, 33, 40]
vazao_acum = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0]

# Tubos
diametros = [150, 200, 250, 300, 400] # em mm
custo = [65.0, 98.0, 150.0, 210.0, 340.0]

populacao = []

for i in range(5):
    
    genes = []
    for j in range(NUM_GENES):
        idx = np.random.randint(low=0, high=5)
        tubo = Tubo(diametros[idx], custo[idx])
        genes.append(Gene(comprimentos[j], vazao_acum[j], tubo))
    populacao.append(Individuo(genes))

populacao = selecao(populacao)

# for indiv in populacao:
#     printa_individuo(indiv)
    