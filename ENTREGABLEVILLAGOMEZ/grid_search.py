"""
grid_search.py
---------------
Implementación de BFS y A* sobre mapas de cuadrícula (grid maps).

Formato del mapa (texto plano):

    S....
    .##..
    ...#.
    .#..G

Símbolos:
    S  -> inicio
    G  -> meta
    .  -> camino libre
    #  -> obstáculo

Cada casilla libre se representa como una coordenada (fila, columna).
"""

import heapq
from collections import deque


def leer_mapa(ruta_archivo):
    """
    Lee un mapa desde un archivo de texto y devuelve:
    - grid: lista de listas con cada carácter del mapa
    - inicio: coordenada (fila, columna) de 'S'
    - meta: coordenada (fila, columna) de 'G'
    """
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        lineas = [linea.rstrip("\n") for linea in f if linea.strip("\n") != ""]

    grid = [list(linea) for linea in lineas]
    inicio = None
    meta = None

    for fila_idx, fila in enumerate(grid):
        for col_idx, valor in enumerate(fila):
            if valor == "S":
                inicio = (fila_idx, col_idx)
            elif valor == "G":
                meta = (fila_idx, col_idx)

    if inicio is None or meta is None:
        raise ValueError("El mapa debe contener un inicio 'S' y una meta 'G'.")

    return grid, inicio, meta


def vecinos_validos(grid, nodo):
    """
    Devuelve las coordenadas vecinas válidas (arriba, abajo, izquierda, derecha)
    que están dentro del mapa y no son obstáculos ('#').
    """
    fila, col = nodo
    filas = len(grid)
    columnas = len(grid[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der

    resultado = []
    for df, dc in movimientos:
        nf, nc = fila + df, col + dc
        if 0 <= nf < filas and 0 <= nc < columnas:
            if grid[nf][nc] != "#":
                resultado.append((nf, nc))
    return resultado


def _reconstruir_camino(padres, meta):
    camino = []
    nodo = meta
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    camino.reverse()
    return camino


def bfs_mapa(grid, inicio, meta, debug=False):
    """BFS sobre un mapa de cuadrícula. Encuentra el camino más corto en número de pasos."""
    frontera = deque([inicio])
    visitados = {inicio}
    padres = {inicio: None}

    while frontera:
        nodo_actual = frontera.popleft()

        if debug:
            print(f"[BFS-mapa] nodo actual: {nodo_actual}")
            print(f"[BFS-mapa] frontera: {list(frontera)}")

        if nodo_actual == meta:
            return _reconstruir_camino(padres, meta)

        for vecino in vecinos_validos(grid, nodo_actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                frontera.append(vecino)
                if debug:
                    print(f"[BFS-mapa] vecino válido: {vecino} | padre: {nodo_actual}")

    return None


def dfs_mapa(grid, inicio, meta, debug=False):
    """DFS sobre un mapa de cuadrícula. No garantiza el camino más corto."""
    pila = [inicio]
    visitados = {inicio}
    padres = {inicio: None}

    while pila:
        nodo_actual = pila.pop()

        if debug:
            print(f"[DFS-mapa] nodo actual: {nodo_actual}")
            print(f"[DFS-mapa] pila: {pila}")

        if nodo_actual == meta:
            return _reconstruir_camino(padres, meta)

        for vecino in vecinos_validos(grid, nodo_actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo_actual
                pila.append(vecino)
                if debug:
                    print(f"[DFS-mapa] vecino válido: {vecino} | padre: {nodo_actual}")

    return None


def heuristica_manhattan(nodo, meta):
    """Distancia Manhattan entre 'nodo' y 'meta'."""
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])


def a_estrella_mapa(grid, inicio, meta, debug=False):
    """
    A* sobre un mapa de cuadrícula.
    f(n) = g(n) + h(n)
      g(n): costo acumulado desde el inicio
      h(n): heurística Manhattan hasta la meta
    """
    contador = 0  # desempate estable en la cola de prioridad
    frontera = [(0, contador, inicio)]  # (f, contador, nodo)
    padres = {inicio: None}
    costo_g = {inicio: 0}
    visitados = set()

    while frontera:
        f_actual, _, nodo_actual = heapq.heappop(frontera)

        if debug:
            print(f"[A*] nodo actual: {nodo_actual} | f(n)={f_actual} | g(n)={costo_g[nodo_actual]}")

        if nodo_actual == meta:
            return _reconstruir_camino(padres, meta), costo_g[meta]

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        for vecino in vecinos_validos(grid, nodo_actual):
            nuevo_costo = costo_g[nodo_actual] + 1  # cada movimiento cuesta 1

            if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo
                h = heuristica_manhattan(vecino, meta)
                f = nuevo_costo + h
                padres[vecino] = nodo_actual
                contador += 1
                heapq.heappush(frontera, (f, contador, vecino))
                if debug:
                    print(f"[A*] vecino válido: {vecino} | g={nuevo_costo} h={h} f={f} | padre: {nodo_actual}")

    return None, None


def imprimir_mapa_con_camino(grid, camino):
    """Imprime el mapa marcando el camino encontrado con '*' (sin sobrescribir S ni G)."""
    grid_copia = [fila[:] for fila in grid]
    if camino:
        for (fila, col) in camino:
            if grid_copia[fila][col] == ".":
                grid_copia[fila][col] = "*"
    for fila in grid_copia:
        print("".join(fila))


if __name__ == "__main__":
    import sys

    ruta = sys.argv[1] if len(sys.argv) > 1 else "maps/map1.txt"
    grid, inicio, meta = leer_mapa(ruta)

    print(f"Mapa: {ruta}")
    print(f"Inicio: {inicio} | Meta: {meta}\n")

    print("=== BFS sobre mapa ===")
    camino_bfs = bfs_mapa(grid, inicio, meta, debug=True)
    print("Camino BFS:", camino_bfs)
    if camino_bfs:
        print(f"Longitud del camino: {len(camino_bfs) - 1} pasos")
        imprimir_mapa_con_camino(grid, camino_bfs)

    print("\n=== A* sobre mapa ===")
    camino_astar, costo = a_estrella_mapa(grid, inicio, meta, debug=True)
    print("Camino A*:", camino_astar)
    if camino_astar:
        print(f"Costo total: {costo}")
        imprimir_mapa_con_camino(grid, camino_astar)
