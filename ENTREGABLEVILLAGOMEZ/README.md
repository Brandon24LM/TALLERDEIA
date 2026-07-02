# Taller: BFS, DFS y A* en Python

Implementación de tres algoritmos de búsqueda (BFS, DFS y A*) aplicados a un
grafo simple y a mapas de cuadrícula, como parte del taller de algoritmos de
búsqueda.

## Estructura del repositorio

```
taller_busquedas/
├── graph_search.py     # BFS y DFS sobre un grafo simple (diccionario)
├── grid_search.py      # BFS, DFS y A* sobre mapas de cuadrícula (texto)
├── main.py             # Ejecuta todo y muestra una tabla comparativa
├── maps/
│   ├── map1.txt         # Mapa de prueba pequeño (5x4)
│   └── map2.txt          # Mapa de prueba más grande, tipo laberinto (11x11)
├── salida_consola.txt   # Captura de la salida de consola al ejecutar main.py
└── README.md
```

## Requisitos

- Python 3.8 o superior (no requiere librerías externas).

## Cómo ejecutar

### 1. Ejecutar todo el taller de una vez

```bash
python3 main.py
```

Esto corre BFS y DFS sobre el grafo de ejemplo, y BFS, DFS y A* sobre los dos
mapas en `maps/`, mostrando el camino encontrado, el mapa con la ruta marcada
(`*`) y una tabla comparativa final con el costo/pasos de cada algoritmo.

### 2. Ejecutar solo el grafo simple

```bash
python3 graph_search.py
```

Muestra las trazas de depuración (nodo actual, frontera/pila, visitados,
vecinos válidos y padre asignado) para BFS y DFS sobre el grafo A–F.

### 3. Ejecutar solo un mapa específico

```bash
python3 grid_search.py maps/map1.txt
python3 grid_search.py maps/map2.txt
```

Muestra las trazas de depuración de BFS y A* (nodo actual, frontera, vecinos
válidos, padres, y en A* también costo acumulado `g(n)` y `f(n)`) y el mapa
final con el camino marcado.

## Formato de los mapas

Los mapas son archivos de texto plano donde:

| Símbolo | Significado     |
|---------|------------------|
| `S`     | Inicio           |
| `G`     | Meta             |
| `.`     | Camino libre     |
| `#`     | Obstáculo        |

El robot solo puede moverse en 4 direcciones: arriba, abajo, izquierda y
derecha (no en diagonal).

## Algoritmos implementados

- **BFS (Breadth-First Search)**: usa una cola (`collections.deque`).
  Garantiza el camino más corto en número de pasos cuando todos los
  movimientos cuestan lo mismo.
- **DFS (Depth-First Search)**: usa una pila. Explora en profundidad antes de
  retroceder; no garantiza el camino más corto.
- **A\***: usa una cola de prioridad (`heapq`) y la fórmula `f(n) = g(n) + h(n)`,
  con `h(n)` calculada como distancia Manhattan hasta la meta. Encuentra el
  camino óptimo explorando de forma más eficiente que BFS al priorizar los
  nodos más prometedores.

## Resultados de prueba

Ver `salida_consola.txt` para la salida completa, o ejecutar `python3 main.py`
para reproducirla. Resumen:

| Algoritmo / Mapa      | Costo / Pasos |
|------------------------|---------------|
| BFS (grafo A→F)        | 2             |
| DFS (grafo A→F)        | 2             |
| BFS (map1.txt)         | 7             |
| DFS (map1.txt)         | 7             |
| A\* (map1.txt)          | 7             |
| BFS (map2.txt)         | 20            |
| DFS (map2.txt)         | 20            |
| A\* (map2.txt)          | 20            |

## Reflexión final

Ver `REFLEXION.md`.
