# Taller: BFS, DFS y A* en Python

Implementación de tres algoritmos de búsqueda de rutas para un robot
que se mueve por un mapa de cuadrícula, evitando obstáculos.

## Estructura del repositorio

```
taller_busqueda/
├── graph_search.py     # Fase 1-3: grafo simple + BFS/DFS sobre grafo
├── grid_search.py      # Fase 4-5: BFS, DFS y A* sobre mapas de cuadrícula
├── main.py             # Ejecuta los algoritmos sobre los mapas de prueba y los compara
├── maps/
│   ├── mapa1.txt        # Mapa de prueba 1 (del enunciado)
│   └── mapa2.txt        # Mapa de prueba 2 (más grande, tipo laberinto)
├── salida_consola.txt   # Salida de ejemplo de la ejecución de main.py
├── reflexion.md         # Reflexión final del equipo
└── README.md
```

## Requisitos

- Python 3.8 o superior (no se necesitan librerías externas).

## Cómo ejecutar

1. Clona o descarga este repositorio.
2. Desde la carpeta `taller_busqueda`, ejecuta:

```bash
python3 main.py
```

Esto correrá BFS, DFS y A* sobre `maps/mapa1.txt` y `maps/mapa2.txt`,
mostrando en consola:

- El camino encontrado por cada algoritmo dibujado sobre el mapa (`*`).
- La longitud del camino en casillas.
- Una comparación final entre los tres algoritmos.

También se puede probar cada módulo por separado:

```bash
python3 graph_search.py   # BFS y DFS sobre el grafo simple de la Fase 1
python3 grid_search.py    # BFS, DFS y A* sobre el mapa del enunciado, con trazas
```

## Formato de los mapas

Los mapas son archivos de texto plano donde:

| Símbolo | Significado   |
|---------|----------------|
| `S`     | Inicio         |
| `G`     | Meta           |
| `.`     | Camino libre   |
| `#`     | Obstáculo      |

Para agregar un mapa nuevo, basta con crear un archivo `.txt` con este
formato dentro de `maps/` y llamar a `ejecutar_sobre_mapa("maps/tu_mapa.txt")`
en `main.py`.

## Algoritmos implementados

- **BFS** (`bfs_mapa`): usa una cola (FIFO). Garantiza el camino más
  corto en un mapa sin pesos, porque explora por niveles de distancia.
- **DFS** (`dfs_mapa`): usa una pila (LIFO). Encuentra *un* camino,
  pero no garantiza que sea el más corto.
- **A\*** (`a_estrella_mapa`): usa una cola de prioridad y la fórmula
  `f(n) = g(n) + h(n)`, con distancia Manhattan como heurística `h(n)`.
  Encuentra el camino más corto explorando, en general, menos nodos
  que BFS.
