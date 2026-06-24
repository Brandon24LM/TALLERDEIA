from pathlib import Path
from src.grid_search import load_grid_from_file, bfs_grid, dfs_grid, astar_grid, render_grid_with_path

BASE_DIR = Path(__file__).resolve().parents[1]


def show_result(name, grid, path):
    print("\n" + "-" * 60)
    print(name)
    print("Camino:", path)
    print("Longitud:", len(path))
    print(render_grid_with_path(grid, path))


def main():
    grid = load_grid_from_file(str(BASE_DIR / "data" / "mapa_obstaculos.txt"))

    show_result("BFS", grid, bfs_grid(grid))
    show_result("DFS", grid, dfs_grid(grid))
    show_result("A*", grid, astar_grid(grid))


if __name__ == "__main__":
    main()
