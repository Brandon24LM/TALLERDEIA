"""Herramientas sencillas para depuración incremental."""
from typing import Any, Iterable


def print_section(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def debug_list(name: str, values: Iterable[Any]) -> None:
    print(f"{name}: {list(values)}")


def assert_path_valid(path: list, start: Any, goal: Any) -> None:
    if not path:
        raise AssertionError("El camino está vacío.")
    if path[0] != start:
        raise AssertionError(f"El camino no inicia en {start!r}. Inicia en {path[0]!r}.")
    if path[-1] != goal:
        raise AssertionError(f"El camino no termina en {goal!r}. Termina en {path[-1]!r}.")
    print("Camino validado correctamente.")
