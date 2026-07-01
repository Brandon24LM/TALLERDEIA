# Algoritmos de búsqueda: BFS, DFS y A*

Proyecto que implementa y compara tres algoritmos de búsqueda de caminos:
**BFS** (búsqueda en anchura), **DFS** (búsqueda en profundidad) y **A\***
(búsqueda informada con heurística), sobre un grafo simple y sobre mapas de
cuadrícula.

## Estructura del repositorio

```
proyecto-busqueda/
├── src/
│   ├── grafo.py         # Grafo de ejemplo (Fase 1)
│   ├── mapas.py          # Lectura de mapas de texto y cálculo de vecinos
│   ├── algoritmos.py     # Implementación de BFS, DFS y A*
│   └── main.py            # Script principal: ejecuta y compara todo
├── mapas/
│   ├── mapa1.txt          # Mapa de prueba pequeño
│   └── mapa2.txt          # Mapa de prueba tipo laberinto serpentina
├── salidas/
│   └── salida_consola.txt # Captura de la salida de consola
├── reflexion.md           # Reflexión final del equipo
└── README.md
```

## Requisitos

- Python 3.8 o superior (no se necesitan librerías externas, solo la
  librería estándar: `collections` y `heapq`).

## Cómo ejecutar

1. Clonar el repositorio y entrar a la carpeta `src`:

   ```bash
   git clone <url-del-repositorio>
   cd proyecto-busqueda/src
   ```

2. Ejecutar el script principal:

   ```bash
   python3 main.py
   ```

   Esto va a:
   - Correr **BFS** y **DFS** sobre el grafo simple de la Fase 1 (`A` → `F`).
   - Correr **BFS**, **DFS** y **A\*** sobre `mapas/mapa1.txt` y
     `mapas/mapa2.txt`, imprimiendo el mapa con el camino encontrado marcado
     con `*`, además de la longitud del camino y la cantidad de nodos
     explorados por cada algoritmo.
   - Imprimir una tabla comparativa al final de cada mapa.

3. Si se quiere guardar la salida en un archivo (como se hizo en
   `salidas/salida_consola.txt`):

   ```bash
   python3 main.py > ../salidas/salida_consola.txt
   ```

## Cómo probar con un mapa propio

Crear un archivo `.txt` dentro de `mapas/` usando estos símbolos:

| Símbolo | Significado   |
|---------|---------------|
| `S`     | Inicio        |
| `G`     | Meta          |
| `.`     | Camino libre  |
| `#`     | Obstáculo     |

Y agregar una llamada `probar_mapa("nombre_del_archivo.txt")` al final de
`main.py`.

## Cómo activar las trazas de depuración

Las funciones `bfs`, `dfs` y `a_estrella` en `algoritmos.py` aceptan un
parámetro opcional `trazas=True`, que imprime en cada iteración la
frontera/pila, los visitados y (en A*) el costo acumulado y el padre
asignado a cada nodo. Ejemplo:

```python
from algoritmos import bfs
camino, explorados = bfs(vecinos_fn, inicio, meta, trazas=True)
```

Esto sigue la estrategia de **depuración por capas** descrita en la Fase 8:
primero se valida que el mapa se lea bien, luego que la frontera crezca y
disminuya correctamente, y finalmente que el camino reconstruido empiece en
`S` y termine en `G`.
