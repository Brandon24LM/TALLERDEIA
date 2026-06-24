# Taller: Programación y depuración incremental de algoritmos de búsqueda en Python

## Tema
Programación y depuración incremental de algoritmos de búsqueda: **BFS, DFS y A\***.

## Propósito del repositorio
Este repositorio contiene una guía completa para aprender, programar, probar y depurar algoritmos de búsqueda en Python. Está pensado para estudiantes que ya conocen estructuras básicas como listas, diccionarios, ciclos y funciones, pero que todavía necesitan aprender a construir algoritmos paso a paso sin caer en el noble deporte humano de escribir 80 líneas y luego preguntarse por qué todo arde.

## Resultados de aprendizaje
Al finalizar el taller, el estudiante podrá:

1. Representar un problema de búsqueda usando grafos y mapas de cuadrícula.
2. Implementar BFS, DFS y A\* en Python.
3. Depurar algoritmos de manera incremental usando trazas, pruebas pequeñas y validación de estados.
4. Comparar BFS, DFS y A\* según completitud, optimalidad, costo y memoria.
5. Explicar qué algoritmo conviene usar según el tipo de problema.

## Estructura del repositorio

```text
taller_busqueda_bfs_dfs_astar_python/
├── README.md
├── TALLER.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── graph_search.py
│   ├── grid_search.py
│   └── debug_tools.py
├── examples/
│   ├── demo_graph.py
│   ├── demo_grid.py
│   └── demo_debug_incremental.py
├── tests/
│   ├── test_graph_search.py
│   └── test_grid_search.py
├── data/
│   ├── mapa_simple.txt
│   └── mapa_obstaculos.txt
└── docs/
    ├── GUIA_DEPURACION.md
    ├── RUBRICA.md
    └── ACTIVIDAD_FINAL.md
```

## Cómo usar este repositorio

### 1. Clonar o descargar

```bash
git clone <URL_DEL_REPOSITORIO>
cd taller_busqueda_bfs_dfs_astar_python
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
```

Activar en Windows:

```bash
.venv\Scripts\activate
```

Activar en Linux/Mac:

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar ejemplos

```bash
python examples/demo_graph.py
python examples/demo_grid.py
python examples/demo_debug_incremental.py
```

### 5. Ejecutar pruebas

```bash
pytest
```

## Algoritmos incluidos

| Algoritmo | Idea principal | Garantiza camino más corto | Usa heurística |
|---|---|---:|---:|
| BFS | Explora por niveles | Sí, si todos los costos son iguales | No |
| DFS | Explora profundo antes de retroceder | No | No |
| A\* | Combina costo acumulado + estimación al objetivo | Sí, si la heurística es admisible | Sí |

## Recomendación para estudiantes
No intentes programar BFS, DFS y A\* completos al mismo tiempo. Primero crea el grafo, luego imprime vecinos, después visita nodos, luego reconstruye el camino y recién ahí te permites sentir que la máquina te obedece.

