"""
Fase 1-3 del taller: representación de un grafo simple y
búsquedas BFS / DFS sobre ese grafo.
"""
from collections import deque

# Grafo de ejemplo (Fase 1)
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def reconstruir_camino(padres, inicio, meta):
    """Reconstruye el camino desde 'inicio' hasta 'meta' usando el
    diccionario de padres. Devuelve None si 'meta' no es alcanzable."""
    if meta not in padres and meta != inicio:
        return None

    camino = [meta]
    while camino[-1] != inicio:
        camino.append(padres[camino[-1]])
    camino.reverse()
    return camino


def bfs_grafo(grafo, inicio, meta, trazas=False):
    """BFS sobre un grafo simple. Usa una cola (FIFO)."""
    frontera = deque([inicio])
    visitados = {inicio}
    padres = {}

    while frontera:
        actual = frontera.popleft()
        if trazas:
            print(f"[BFS] actual={actual} frontera={list(frontera)} visitados={visitados}")

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.add(vecino)  # se marca ANTES de encolar
                padres[vecino] = actual
                frontera.append(vecino)
                if trazas:
                    print(f"       vecino válido={vecino} padre={actual}")

    return None


def dfs_grafo(grafo, inicio, meta, trazas=False):
    """DFS sobre un grafo simple. Usa una pila (LIFO)."""
    frontera = [inicio]
    visitados = {inicio}
    padres = {}

    while frontera:
        actual = frontera.pop()
        if trazas:
            print(f"[DFS] actual={actual} frontera={frontera} visitados={visitados}")

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in grafo.get(actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                frontera.append(vecino)
                if trazas:
                    print(f"       vecino válido={vecino} padre={actual}")

    return None


if __name__ == "__main__":
    print("Grafo:", grafo)
    print("BFS A->F:", bfs_grafo(grafo, "A", "F", trazas=True))
    print("DFS A->F:", dfs_grafo(grafo, "A", "F", trazas=True))
