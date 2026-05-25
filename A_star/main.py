import heapq
import math

def calcular_heuristica(atual, destino):
    return math.sqrt((atual[0] - destino[0])**2 + (atual[1] - destino[1])**2)

def algoritmo_a_star(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])

    inicio = None
    fim = None

    # Encontrar as coordenadas de inicio e fim
    for r in range(linhas):
        for c in range(colunas):
            if mapa[r][c] == 'I':
                inicio = (r, c)
            elif mapa[r][c] == 'F':
                fim = (r, c)

    if not inicio or not fim:
        print("O mapa deve conter um ponto 'I' e um ponto 'F'.")
        return
    
    # Estrutura de dados
    # (F, contador, G, (linha, coluna), caminho_percorrido)
    lista_aberta = []
    contador = 0
    
    # Inicialmente o custo em 'I' é 0. E o caminho percorrido tbm é 'I'
    heapq.heappush(lista_aberta, (0, contador, 0, inicio, [inicio]))

    # Dicionário para encontrar o menor G de cada célula
    melhor_g = { inicio: 0 }

    # lista de células expandidas
    celulas_expandidas = set()

    # Movimentos possíveis: Direita, Baixo, Esquerda, Cima
    direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while lista_aberta:

        #Pega a célula com menor custo F
        f, _, g_atual, atual, caminho = heapq.heappop(lista_aberta)

        if atual in celulas_expandidas:
            continue

        celulas_expandidas.add(atual)

        if atual == fim:
            return caminho, g_atual
        
        # Explora as direções distintas
        for dr, dc in direcoes:
            vizinho_r, vizinho_c = atual[0] + dr, atual[1] + dc
            vizinho = (vizinho_r, vizinho_c)

            if 0 <= vizinho_r < linhas and 0 <= vizinho_c < colunas:
                valor_celula = mapa[vizinho_r][vizinho_c]

                # Caminho bloqueado
                if valor_celula == '*':
                    continue

                # Descobrir o custo para pisar na célula vizinha
                custo_passo = 0
                if valor_celula != 'F' and valor_celula != 'I':
                    custo_passo = int(valor_celula)

                # Calcula o novo custo acumulado (G)
                novo_g = g_atual + custo_passo
                
                if vizinho not in melhor_g or novo_g < melhor_g[vizinho]:
                    melhor_g[vizinho] = novo_g

                    # Calcular a heurística (h) e o custo total (F)
                    h = calcular_heuristica(vizinho, fim)
                    novo_f = novo_g + h

                    # Atualizar caminho
                    novo_caminho = caminho + [vizinho]

                    # Adicionar à lista aberta
                    contador += 1
                    heapq.heappush(lista_aberta, (novo_f, contador, novo_g, vizinho, novo_caminho))
    return None, 0

mapa_exemplo_1 = [
    ['I', '2', '1', '1', '1', '2'],
    ['1', '*', '2', '*', '3', '1'],
    ['1', '4', '15', '*', '*', '1'],
    ['2', '*', '15', '*', '4', '1'],
    ['*', '*', '2', '2', '9', '2'],
    ['*', '*', '*', '*', 'F', '1']
]

caminho_encontrado, custo_total = algoritmo_a_star(mapa_exemplo_1)

print("Caminho:", caminho_encontrado)
print("Custo:", custo_total)