"""Algoritmos de búsqueda sobre mapas de cuadrícula.

Mapa permitido:
S = inicio
G = meta
. = celda libre
# = obstáculo
"""
from collections import deque
import heapq
import textwrap
from typing import Dict, Iterable, List, Optional, Set, Tuple

Position = Tuple[int, int]
Grid = List[List[str]]


def load_grid_from_text(text: str) -> Grid:
    """Convierte texto multilínea en una cuadrícula."""
    clean_text = textwrap.dedent(text).strip()
    lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("El mapa está vacío.")

    width = len(lines[0])
    if any(len(line) != width for line in lines):
        raise ValueError("Todas las filas del mapa deben tener el mismo ancho.")

    grid = [list(line) for line in lines]
    return grid


def load_grid_from_file(path: str) -> Grid:
    """Carga un mapa desde un archivo de texto."""
    with open(path, "r", encoding="utf-8") as file:
        return load_grid_from_text(file.read())


def find_symbol(grid: Grid, symbol: str) -> Position:
    """Busca una posición por símbolo."""
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == symbol:
                return (row_index, col_index)
    raise ValueError(f"No se encontró el símbolo {symbol!r} en el mapa.")


def in_bounds(grid: Grid, position: Position) -> bool:
    row, col = position
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def passable(grid: Grid, position: Position) -> bool:
    row, col = position
    return grid[row][col] != "#"


def neighbors(grid: Grid, position: Position) -> Iterable[Position]:
    """Retorna vecinos válidos: arriba, abajo, izquierda y derecha."""
    row, col = position
    candidates = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
    ]
    for candidate in candidates:
        if in_bounds(grid, candidate) and passable(grid, candidate):
            yield candidate


def reconstruct_path(came_from: Dict[Position, Optional[Position]], start: Position, goal: Position) -> List[Position]:
    if goal not in came_from:
        return []

    path = []
    current: Optional[Position] = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path if path and path[0] == start else []


def bfs_grid(grid: Grid, start: Optional[Position] = None, goal: Optional[Position] = None, debug: bool = False) -> List[Position]:
    """BFS aplicado a una cuadrícula."""
    start = start or find_symbol(grid, "S")
    goal = goal or find_symbol(grid, "G")

    frontier = deque([start])
    visited: Set[Position] = {start}
    came_from: Dict[Position, Optional[Position]] = {start: None}

    while frontier:
        current = frontier.popleft()
        if debug:
            print(f"[BFS-GRID] Actual: {current} | Frontera: {list(frontier)}")

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)
    return []


def dfs_grid(grid: Grid, start: Optional[Position] = None, goal: Optional[Position] = None, debug: bool = False) -> List[Position]:
    """DFS aplicado a una cuadrícula."""
    start = start or find_symbol(grid, "S")
    goal = goal or find_symbol(grid, "G")

    frontier = [start]
    visited: Set[Position] = {start}
    came_from: Dict[Position, Optional[Position]] = {start: None}

    while frontier:
        current = frontier.pop()
        if debug:
            print(f"[DFS-GRID] Actual: {current} | Pila: {frontier}")

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in neighbors(grid, current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)
    return []


def manhattan(a: Position, b: Position) -> int:
    """Distancia Manhattan para mapas con movimiento ortogonal."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_grid(grid: Grid, start: Optional[Position] = None, goal: Optional[Position] = None, debug: bool = False) -> List[Position]:
    """A* aplicado a una cuadrícula con costo uniforme por movimiento."""
    start = start or find_symbol(grid, "S")
    goal = goal or find_symbol(grid, "G")

    frontier: List[Tuple[int, Position]] = []
    heapq.heappush(frontier, (0, start))

    came_from: Dict[Position, Optional[Position]] = {start: None}
    cost_so_far: Dict[Position, int] = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if debug:
            print(f"[A*] Actual: {current} | Costo: {cost_so_far[current]} | Prioridad pendiente: {frontier}")

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor in neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

                if debug:
                    print(f"  Vecino: {neighbor} | g={new_cost} | h={manhattan(neighbor, goal)} | f={priority}")

    return []


def render_grid_with_path(grid: Grid, path: List[Position]) -> str:
    """Dibuja el mapa agregando '*' sobre el camino encontrado."""
    copy = [row[:] for row in grid]
    for row, col in path:
        if copy[row][col] not in {"S", "G"}:
            copy[row][col] = "*"
    return "\n".join("".join(row) for row in copy)
