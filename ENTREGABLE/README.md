"""
algoritmos.py
Implementaciones de BFS, DFS y A* para grafos y mapas de cuadricula.
"""

from collections import deque
import heapq


# ---------------------------------------------------------------------------
# Utilidad comun: reconstruir camino a partir del diccionario de padres
# ---------------------------------------------------------------------------
def reconstruir_camino(padres, inicio, meta):
    if meta not in padres:
        return None
    camino = [meta]
    while camino[-1] != inicio:
        camino.append(padres[camino[-1]])
    camino.reverse()
    return camino


# ---------------------------------------------------------------------------
# BFS (Busqueda en anchura) - funciona sobre grafos (dict) y sobre mapas
# (siempre que se le pase una funcion vecinos(nodo) -> lista de nodos)
# ---------------------------------------------------------------------------
def bfs(vecinos_fn, inicio, meta, trazas=False):
    """
    vecinos_fn: funcion que recibe un nodo y devuelve sus vecinos (lista)
    inicio, meta: nodos (pueden ser str en grafo, o tupla (fila, col) en mapa)
    """
    cola = deque([inicio])
    # IMPORTANTE: se marca visitado al ENTRAR a la cola, no al salir.
    # Este es el error frecuente descrito en la Fase 2: si se marca tarde,
    # un mismo nodo puede entrar varias veces a la cola.
    visitados = {inicio}
    padres = {inicio: None}
    nodos_explorados = 0

    while cola:
        if trazas:
            print(f"  Frontera: {list(cola)} | Visitados: {visitados}")

        nodo_actual = cola.popleft()
        nodos_explorados += 1

        if nodo_actual == meta:
            return reconstruir_camino(padres, inicio, meta), nodos_explorados

        for vecino in vecinos_fn(nodo_actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                cola.append(vecino)

    return None, nodos_explorados


# ---------------------------------------------------------------------------
# DFS (Busqueda en profundidad) - misma estructura que BFS pero con pila
# ---------------------------------------------------------------------------
def dfs(vecinos_fn, inicio, meta, trazas=False):
    pila = [inicio]
    visitados = {inicio}
    padres = {inicio: None}
    nodos_explorados = 0

    while pila:
        if trazas:
            print(f"  Pila: {pila} | Visitados: {visitados}")

        nodo_actual = pila.pop()  # diferencia clave: ultimo en entrar, primero en salir
        nodos_explorados += 1

        if nodo_actual == meta:
            return reconstruir_camino(padres, inicio, meta), nodos_explorados

        for vecino in vecinos_fn(nodo_actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                pila.append(vecino)

    return None, nodos_explorados


# ---------------------------------------------------------------------------
# A* - requiere coordenadas (fila, col) para poder calcular la heuristica
# ---------------------------------------------------------------------------
def heuristica_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_estrella(vecinos_fn, inicio, meta, trazas=False):
    contador = 0  # desempata cuando dos nodos tienen el mismo f(n)
    frontera = [(0, contador, inicio)]
    padres = {inicio: None}
    costo_g = {inicio: 0}
    nodos_explorados = 0

    while frontera:
        if trazas:
            vista = [(f, n) for f, _, n in frontera]
            print(f"  Frontera (f, nodo): {vista}")

        f_actual, _, nodo_actual = heapq.heappop(frontera)
        nodos_explorados += 1

        if nodo_actual == meta:
            return reconstruir_camino(padres, inicio, meta), costo_g[meta], nodos_explorados

        for vecino in vecinos_fn(nodo_actual):
            nuevo_costo = costo_g[nodo_actual] + 1  # cada paso cuesta 1

            if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo
                f = nuevo_costo + heuristica_manhattan(vecino, meta)
                contador += 1
                heapq.heappush(frontera, (f, contador, vecino))
                padres[vecino] = nodo_actual
                if trazas:
                    print(f"    Padre asignado: {vecino} -> {nodo_actual} | g={nuevo_costo} f={f}")

    return None, None, nodos_explorados
