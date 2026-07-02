"""
main.py
--------
Ejecuta BFS y DFS sobre el grafo simple del taller, y BFS, DFS y A*
sobre los dos mapas de prueba (maps/map1.txt y maps/map2.txt).
Al final imprime una tabla comparativa de resultados.

Uso:
    python3 main.py
"""

from graph_search import bfs_grafo, dfs_grafo
from grid_search import (
    leer_mapa,
    bfs_mapa,
    dfs_mapa,
    a_estrella_mapa,
    imprimir_mapa_con_camino,
)


def separador(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


def probar_grafo():
    separador("PARTE 1: Grafo simple (A -> F)")

    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }

    camino_bfs = bfs_grafo(grafo, "A", "F")
    camino_dfs = dfs_grafo(grafo, "A", "F")

    print("Camino BFS:", camino_bfs)
    print("Camino DFS:", camino_dfs)

    return {
        "BFS (grafo)": len(camino_bfs) - 1 if camino_bfs else None,
        "DFS (grafo)": len(camino_dfs) - 1 if camino_dfs else None,
    }


def probar_mapa(ruta_mapa):
    separador(f"PARTE 2: Mapa {ruta_mapa}")

    grid, inicio, meta = leer_mapa(ruta_mapa)
    print(f"Inicio: {inicio} | Meta: {meta}\n")

    print("--- BFS ---")
    camino_bfs = bfs_mapa(grid, inicio, meta)
    if camino_bfs:
        print(f"Pasos: {len(camino_bfs) - 1}")
        imprimir_mapa_con_camino(grid, camino_bfs)
    else:
        print("No se encontró camino.")

    print("\n--- DFS ---")
    camino_dfs = dfs_mapa(grid, inicio, meta)
    if camino_dfs:
        print(f"Pasos: {len(camino_dfs) - 1}")
        imprimir_mapa_con_camino(grid, camino_dfs)
    else:
        print("No se encontró camino.")

    print("\n--- A* ---")
    camino_astar, costo = a_estrella_mapa(grid, inicio, meta)
    if camino_astar:
        print(f"Costo: {costo}")
        imprimir_mapa_con_camino(grid, camino_astar)
    else:
        print("No se encontró camino.")

    return {
        f"BFS ({ruta_mapa})": len(camino_bfs) - 1 if camino_bfs else None,
        f"DFS ({ruta_mapa})": len(camino_dfs) - 1 if camino_dfs else None,
        f"A* ({ruta_mapa})": costo if camino_astar else None,
    }


def main():
    resultados = {}
    resultados.update(probar_grafo())
    resultados.update(probar_mapa("maps/map1.txt"))
    resultados.update(probar_mapa("maps/map2.txt"))

    separador("TABLA COMPARATIVA DE RESULTADOS")
    print(f"{'Algoritmo / Mapa':<25}{'Costo / Pasos':>15}")
    print("-" * 40)
    for clave, valor in resultados.items():
        print(f"{clave:<25}{str(valor):>15}")


if __name__ == "__main__":
    main()
