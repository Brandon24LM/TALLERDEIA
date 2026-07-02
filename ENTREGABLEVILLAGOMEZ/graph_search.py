"""
graph_search.py
----------------
Implementación de BFS y DFS sobre un grafo simple (no ponderado),
representado como un diccionario de listas de adyacencia.

Ejemplo de grafo usado en el taller:

grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
"""

from collections import deque


def bfs_grafo(grafo, inicio, meta, debug=False):
    """
    Búsqueda en anchura (BFS) sobre un grafo no ponderado.
    Encuentra el camino más corto (en número de aristas) entre
    'inicio' y 'meta'.

    Devuelve la lista de nodos del camino, o None si no hay camino.
    """
    frontera = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}

    while frontera:
        nodo_actual = frontera.popleft()

        if debug:
            print(f"[BFS] nodo actual: {nodo_actual}")
            print(f"[BFS] frontera: {list(frontera)}")
            print(f"[BFS] visitados: {visitados}")

        if nodo_actual == meta:
            return _reconstruir_camino(padres, meta)

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)          # se marca visitado al encontrarlo
                padres[vecino] = nodo_actual
                frontera.append(vecino)
                if debug:
                    print(f"[BFS] vecino válido: {vecino} | padre asignado: {nodo_actual}")

    return None


def dfs_grafo(grafo, inicio, meta, debug=False):
    """
    Búsqueda en profundidad (DFS) sobre un grafo no ponderado.
    No garantiza el camino más corto, pero explora en profundidad
    antes de retroceder.

    Devuelve la lista de nodos del camino, o None si no hay camino.
    """
    pila = [inicio]
    visitados = {inicio}
    padres = {inicio: None}

    while pila:
        nodo_actual = pila.pop()

        if debug:
            print(f"[DFS] nodo actual: {nodo_actual}")
            print(f"[DFS] pila: {pila}")
            print(f"[DFS] visitados: {visitados}")

        if nodo_actual == meta:
            return _reconstruir_camino(padres, meta)

        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                pila.append(vecino)
                if debug:
                    print(f"[DFS] vecino válido: {vecino} | padre asignado: {nodo_actual}")

    return None


def _reconstruir_camino(padres, meta):
    """Reconstruye el camino desde 'meta' hasta el inicio usando el diccionario de padres."""
    camino = []
    nodo = meta
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    return camino


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    print("=== BFS sobre grafo (A -> F) ===")
    camino_bfs = bfs_grafo(grafo, "A", "F", debug=True)
    print("Camino BFS:", camino_bfs)

    print("\n=== DFS sobre grafo (A -> F) ===")
    camino_dfs = dfs_grafo(grafo, "A", "F", debug=True)
    print("Camino DFS:", camino_dfs)
