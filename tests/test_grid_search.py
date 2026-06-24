from src.grid_search import load_grid_from_text, bfs_grid, astar_grid, find_symbol


def test_bfs_grid_finds_path():
    grid = load_grid_from_text("""
    S..
    .#.
    ..G
    """)
    path = bfs_grid(grid)
    assert path[0] == find_symbol(grid, "S")
    assert path[-1] == find_symbol(grid, "G")


def test_astar_grid_finds_path():
    grid = load_grid_from_text("""
    S..
    .#.
    ..G
    """)
    path = astar_grid(grid)
    assert path[0] == find_symbol(grid, "S")
    assert path[-1] == find_symbol(grid, "G")


def test_astar_and_bfs_same_length_on_uniform_grid():
    grid = load_grid_from_text("""
    S....
    .##..
    ...#.
    .#..G
    """)
    assert len(astar_grid(grid)) == len(bfs_grid(grid))
