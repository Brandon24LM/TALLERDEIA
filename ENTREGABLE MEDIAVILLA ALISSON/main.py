"""
Script principal del entregable.
Lee los mapas de la carpeta 'maps/', ejecuta BFS, DFS y A* sobre cada
uno, y muestra una comparación de resultados (longitud de camino y
número de nodos visitados).
"""
from grid_search import (
    leer_mapa,
    bfs_mapa,
    dfs_mapa,
    a_estrella_mapa,
    imprimir_mapa_con_camino,
)


def ejecutar_sobre_mapa(ruta_mapa):
    with open(ruta_mapa, encoding="utf-8") as f:
        texto = f.read()

    mapa, inicio, meta = leer_mapa(texto)

    print(f"\n{'=' * 50}")
    print(f"Mapa: {ruta_mapa}")
    print(f"Inicio: {inicio}  Meta: {meta}")
    print(f"{'=' * 50}")

    resultados = {}
    for nombre, funcion in (
        ("BFS", bfs_mapa),
        ("DFS", dfs_mapa),
        ("A*", a_estrella_mapa),
    ):
        camino = funcion(mapa, inicio, meta)
        largo = len(camino) if camino else None
        resultados[nombre] = largo

        print(f"\n--- {nombre} ---")
        if camino:
            print(f"Longitud del camino: {largo} casillas")
            imprimir_mapa_con_camino(mapa, camino)
        else:
            print("No se encontró camino.")

    print("\nComparación de longitudes de camino:")
    for nombre, largo in resultados.items():
        print(f"  {nombre}: {largo}")


if __name__ == "__main__":
    ejecutar_sobre_mapa("maps/mapa1.txt")
    ejecutar_sobre_mapa("maps/mapa2.txt")
