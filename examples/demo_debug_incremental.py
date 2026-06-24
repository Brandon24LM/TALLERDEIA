from src.grid_search import load_grid_from_text, find_symbol, neighbors, bfs_grid, astar_grid, render_grid_with_path
from src.debug_tools import print_section, debug_list, assert_path_valid


def main():
    mapa = """
    S....
    .##..
    ...#.
    .#..G
    """
    grid = load_grid_from_text(mapa)

    print_section("1. Mapa cargado")
    for row in grid:
        print("".join(row))

    start = find_symbol(grid, "S")
    goal = find_symbol(grid, "G")

    print_section("2. Inicio y meta")
    print("Inicio:", start)
    print("Meta:", goal)

    print_section("3. Vecinos del inicio")
    debug_list("Vecinos", neighbors(grid, start))

    print_section("4. BFS con trazas")
    bfs_path = bfs_grid(grid, start, goal, debug=True)
    print(render_grid_with_path(grid, bfs_path))
    assert_path_valid(bfs_path, start, goal)

    print_section("5. A* con trazas")
    astar_path = astar_grid(grid, start, goal, debug=True)
    print(render_grid_with_path(grid, astar_path))
    assert_path_valid(astar_path, start, goal)


if __name__ == "__main__":
    main()
