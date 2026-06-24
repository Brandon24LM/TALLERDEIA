from src.graph_search import bfs, dfs


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    print("BFS A -> F:", bfs(graph, "A", "F", debug=True))
    print("DFS A -> F:", dfs(graph, "A", "F", debug=True))


if __name__ == "__main__":
    main()
