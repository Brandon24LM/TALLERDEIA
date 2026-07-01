"""
main.py
Ejecuta BFS, DFS y A* sobre el grafo de ejemplo y sobre dos mapas de
cuadricula, e imprime los resultados para comparar.
"""

import os
from grafo import grafo_ejemplo
from mapas import leer_mapa, vecinos_grid, imprimir_mapa_con_camino
from algoritmos import bfs, dfs, a_estrella


def separador(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def probar_grafo():
    separador("PARTE 1: GRAFO SIMPLE (Fase 1-3)")
    print("Grafo:", grafo_ejemplo)

    vecinos_fn = lambda nodo: grafo_ejemplo[nodo]

    camino_bfs, exp_bfs = bfs(vecinos_fn, "A", "F")
    print(f"\nBFS  A -> F : camino = {camino_bfs} | nodos explorados = {exp_bfs}")

    camino_dfs, exp_dfs = dfs(vecinos_fn, "A", "F")
    print(f"DFS  A -> F : camino = {camino_dfs} | nodos explorados = {exp_dfs}")


def probar_mapa(nombre_archivo):
    separador(f"PARTE 2: MAPA '{nombre_archivo}' (Fase 4-5)")

    ruta = os.path.join(os.path.dirname(__file__), "..", "mapas", nombre_archivo)
    with open(ruta, encoding="utf-8") as f:
        mapa_texto = [linea.rstrip("\n") for linea in f if linea.strip("\n") != ""]

    libres, inicio, meta = leer_mapa(mapa_texto)
    print("Mapa original:")
    for fila in mapa_texto:
        print(fila)
    print(f"\nInicio: {inicio} | Meta: {meta} | Casillas libres: {len(libres)}")

    vecinos_fn = lambda nodo: vecinos_grid(nodo, libres)

    # BFS
    camino_bfs, exp_bfs = bfs(vecinos_fn, inicio, meta)
    print(f"\n--- BFS ---")
    print(f"Longitud del camino: {len(camino_bfs) if camino_bfs else 'sin solucion'}")
    print(f"Nodos explorados: {exp_bfs}")
    if camino_bfs:
        imprimir_mapa_con_camino(mapa_texto, camino_bfs)

    # DFS
    camino_dfs, exp_dfs = dfs(vecinos_fn, inicio, meta)
    print(f"\n--- DFS ---")
    print(f"Longitud del camino: {len(camino_dfs) if camino_dfs else 'sin solucion'}")
    print(f"Nodos explorados: {exp_dfs}")
    if camino_dfs:
        imprimir_mapa_con_camino(mapa_texto, camino_dfs)

    # A*
    camino_astar, costo, exp_astar = a_estrella(vecinos_fn, inicio, meta)
    print(f"\n--- A* ---")
    print(f"Longitud del camino: {len(camino_astar) if camino_astar else 'sin solucion'}")
    print(f"Costo total: {costo}")
    print(f"Nodos explorados: {exp_astar}")
    if camino_astar:
        imprimir_mapa_con_camino(mapa_texto, camino_astar)

    # Comparacion resumida
    print(f"\n--- Comparacion en '{nombre_archivo}' ---")
    print(f"{'Algoritmo':<10}{'Longitud camino':<18}{'Nodos explorados':<18}")
    print(f"{'BFS':<10}{len(camino_bfs) if camino_bfs else '-':<18}{exp_bfs:<18}")
    print(f"{'DFS':<10}{len(camino_dfs) if camino_dfs else '-':<18}{exp_dfs:<18}")
    print(f"{'A*':<10}{len(camino_astar) if camino_astar else '-':<18}{exp_astar:<18}")


if __name__ == "__main__":
    probar_grafo()
    probar_mapa("mapa1.txt")
    probar_mapa("mapa2.txt")
