"""Algoritmos de búsqueda sobre grafos simples.

Este módulo implementa BFS y DFS usando programación clara y depuración opcional.
"""
from collections import deque
from typing import Dict, Hashable, Iterable, List, Optional, Set

Graph = Dict[Hashable, Iterable[Hashable]]


def reconstruct_path(came_from: Dict[Hashable, Optional[Hashable]], start: Hashable, goal: Hashable) -> List[Hashable]:
    """Reconstruye el camino desde start hasta goal usando el diccionario de padres."""
    if goal not in came_from:
        return []

    path = []
    current: Optional[Hashable] = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path if path and path[0] == start else []


def bfs(graph: Graph, start: Hashable, goal: Hashable, debug: bool = False) -> List[Hashable]:
    """Búsqueda en anchura.

    Retorna un camino desde start hasta goal. En grafos sin pesos, BFS retorna
    un camino con el menor número de aristas.
    """
    if start not in graph:
        raise ValueError(f"El nodo inicial {start!r} no existe en el grafo.")
    if goal not in graph:
        raise ValueError(f"El nodo meta {goal!r} no existe en el grafo.")

    frontier = deque([start])
    visited: Set[Hashable] = {start}
    came_from: Dict[Hashable, Optional[Hashable]] = {start: None}

    while frontier:
        current = frontier.popleft()

        if debug:
            print(f"[BFS] Actual: {current} | Frontera: {list(frontier)} | Visitados: {visited}")

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)

                if debug:
                    print(f"  Vecino agregado: {neighbor} | Padre: {current}")

    return []


def dfs(graph: Graph, start: Hashable, goal: Hashable, debug: bool = False) -> List[Hashable]:
    """Búsqueda en profundidad.

    Retorna un camino desde start hasta goal si existe. No garantiza el camino
    más corto, porque explora profundo antes de explorar por niveles.
    """
    if start not in graph:
        raise ValueError(f"El nodo inicial {start!r} no existe en el grafo.")
    if goal not in graph:
        raise ValueError(f"El nodo meta {goal!r} no existe en el grafo.")

    frontier = [start]
    visited: Set[Hashable] = {start}
    came_from: Dict[Hashable, Optional[Hashable]] = {start: None}

    while frontier:
        current = frontier.pop()

        if debug:
            print(f"[DFS] Actual: {current} | Pila: {frontier} | Visitados: {visited}")

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        # reverse permite una exploración más predecible en ejemplos didácticos.
        for neighbor in reversed(list(graph[current])):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)

                if debug:
                    print(f"  Vecino agregado: {neighbor} | Padre: {current}")

    return []
