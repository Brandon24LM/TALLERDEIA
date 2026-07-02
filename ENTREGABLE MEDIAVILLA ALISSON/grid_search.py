"""
Fase 4-5 del taller: búsqueda sobre mapas de cuadrícula (BFS, DFS y A*).

Símbolos del mapa:
    S -> inicio
    G -> meta
    . -> camino libre
    # -> obstáculo
"""
from collections import deque
import heapq


def leer_mapa(texto_mapa):
    """Convierte un mapa en texto a una lista de listas de caracteres,
    y localiza inicio (S) y meta (G)."""
    filas = [list(linea) for linea in texto_mapa.strip("\n").split("\n")]
    inicio = meta = None
    for f, fila in enumerate(filas):
        for c, valor in enumerate(fila):
            if valor == "S":
                inicio = (f, c)
            elif valor == "G":
                meta = (f, c)

    if inicio is None or meta is None:
        raise ValueError("El mapa debe tener un 'S' (inicio) y una 'G' (meta)")

    return filas, inicio, meta


def vecinos_validos(mapa, nodo):
    """Devuelve las casillas adyacentes (arriba, abajo, izq, der) que
    existen dentro del mapa y no son obstáculo."""
    filas = len(mapa)
    cols = len(mapa[0])
    f, c = nodo
    candidatos = [(f - 1, c), (f + 1, c), (f, c - 1), (f, c + 1)]

    resultado = []
    for nf, nc in candidatos:
        if 0 <= nf < filas and 0 <= nc < cols and mapa[nf][nc] != "#":
            resultado.append((nf, nc))
    return resultado


def reconstruir_camino(padres, inicio, meta):
    if meta not in padres and meta != inicio:
        return None
    camino = [meta]
    while camino[-1] != inicio:
        camino.append(padres[camino[-1]])
    camino.reverse()
    return camino


def bfs_mapa(mapa, inicio, meta, trazas=False):
    frontera = deque([inicio])
    visitados = {inicio}
    padres = {}

    while frontera:
        actual = frontera.popleft()
        if trazas:
            print(f"[BFS] actual={actual} frontera={list(frontera)}")

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in vecinos_validos(mapa, actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                frontera.append(vecino)

    return None


def dfs_mapa(mapa, inicio, meta, trazas=False):
    frontera = [inicio]
    visitados = {inicio}
    padres = {}

    while frontera:
        actual = frontera.pop()
        if trazas:
            print(f"[DFS] actual={actual} frontera={frontera}")

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in vecinos_validos(mapa, actual):
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = actual
                frontera.append(vecino)

    return None


def heuristica_manhattan(nodo, meta):
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])


def a_estrella_mapa(mapa, inicio, meta, trazas=False):
    """A* usando distancia Manhattan como heurística."""
    contador = 0  # desempata en la cola de prioridad
    frontera = [(0, contador, inicio)]
    padres = {}
    costo_g = {inicio: 0}

    while frontera:
        _, _, actual = heapq.heappop(frontera)
        if trazas:
            print(f"[A*] actual={actual} g={costo_g[actual]}")

        if actual == meta:
            return reconstruir_camino(padres, inicio, meta)

        for vecino in vecinos_validos(mapa, actual):
            nuevo_costo = costo_g[actual] + 1  # cada paso cuesta 1
            if vecino not in costo_g or nuevo_costo < costo_g[vecino]:
                costo_g[vecino] = nuevo_costo
                f = nuevo_costo + heuristica_manhattan(vecino, meta)
                contador += 1
                padres[vecino] = actual
                heapq.heappush(frontera, (f, contador, vecino))

    return None


def imprimir_mapa_con_camino(mapa, camino):
    """Dibuja el camino encontrado sobre el mapa usando '*'."""
    copia = [fila[:] for fila in mapa]
    for (f, c) in camino:
        if copia[f][c] not in ("S", "G"):
            copia[f][c] = "*"
    for fila in copia:
        print("".join(fila))


if __name__ == "__main__":
    mapa_texto = """
S....
.##..
...#.
.#..G
"""
    mapa, inicio, meta = leer_mapa(mapa_texto)
    print("Inicio:", inicio, "Meta:", meta)

    print("\n--- BFS ---")
    camino_bfs = bfs_mapa(mapa, inicio, meta, trazas=True)
    print("Camino BFS:", camino_bfs)
    imprimir_mapa_con_camino(mapa, camino_bfs)

    print("\n--- DFS ---")
    camino_dfs = dfs_mapa(mapa, inicio, meta, trazas=True)
    print("Camino DFS:", camino_dfs)
    imprimir_mapa_con_camino(mapa, camino_dfs)

    print("\n--- A* ---")
    camino_astar = a_estrella_mapa(mapa, inicio, meta, trazas=True)
    print("Camino A*:", camino_astar)
    imprimir_mapa_con_camino(mapa, camino_astar)
