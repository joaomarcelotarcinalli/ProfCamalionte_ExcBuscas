DISTANCIA = 0
ANTERIOR = 1
INFINITO = float("inf")

map = {
    "A":{"B":4,"C":3},
    "B":{"A":4,"C":5,"D":2},
    "C":{"A":3,"B":5,"D":1,"E":3},
    "D":{"B":2,"C":1,"E":4},
    "E":{"C":3,"D":4}
}

tabela = {
    "A":[0,None],
    "B":[INFINITO,None],
    "C":[INFINITO,None],
    "D":[INFINITO,None],
    "E":[INFINITO,None]
}


def get_menor_distancia(tabela: dict, vertice: str) -> int:
    print(tabela[vertice][DISTANCIA])
    return tabela[vertice][DISTANCIA]


def set_menor_distancia(tabela: dict, vertice: str, distancia: int):

    tabela[vertice][DISTANCIA] = distancia


def set_anterior(tabela: dict, vertice: str, anterior: str):

    tabela[vertice][ANTERIOR] = anterior


def get_distancia(map: dict, primeiro_vertice: str, segundo_vertice: str):

    return map[primeiro_vertice][segundo_vertice]


def get_proximo_vertice(tabela: dict, visitado: list):

    unvisited = list(
        set(
            tabela.keys()
        ).difference(visitado)
    )

    min_vertice = unvisited[0]
    min_distancia = tabela[unvisited[0]][DISTANCIA]

    for vertice in unvisited:
        if tabela[vertice][DISTANCIA] < min_distancia:
            min_vertice = vertice
            min_distancia = tabela[vertice][DISTANCIA]
    
    return min_vertice


def acha_menor_caminho(map: dict, tabela: dict, origem: str):

    visitado = []
    atual = origem
    comeco = origem

    while True:
        adjacent_vertice = map[atual]

        if set(adjacent_vertice).issubset(set(visitado)):
            ...
        else:
            unvisted = set(adjacent_vertice).difference(set(visitado))

            for vertice in unvisted:
                distancia_comeco = get_menor_distancia(tabela, vertice)

                if distancia_comeco == INFINITO and atual == comeco:
                    total_distance = get_distancia(map, vertice, atual)
                else:
                    total_distance = get_menor_distancia(tabela, atual)
                    total_distance += get_distancia(map, atual, vertice)

                if total_distance < distancia_comeco:
                    set_menor_distancia(tabela, vertice, total_distance)
                    set_anterior(tabela, vertice, atual)
                    
        visitado.append(atual)
                
        if len(visitado) == len(tabela.keys()):
            break

        atual = get_proximo_vertice(tabela, visitado)

    return tabela



result = acha_menor_caminho(map,tabela,"A")
print(result)