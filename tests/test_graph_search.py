from src.graph_search import bfs, dfs


def sample_graph():
    return {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }


def test_bfs_finds_short_path():
    path = bfs(sample_graph(), "A", "F")
    assert path == ["A", "C", "F"]


def test_dfs_finds_a_path():
    path = dfs(sample_graph(), "A", "F")
    assert path[0] == "A"
    assert path[-1] == "F"
