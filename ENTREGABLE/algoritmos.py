
============================================================
PARTE 1: GRAFO SIMPLE (Fase 1-3)
============================================================
Grafo: {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}

BFS  A -> F : camino = ['A', 'C', 'F'] | nodos explorados = 6
DFS  A -> F : camino = ['A', 'C', 'F'] | nodos explorados = 3

============================================================
PARTE 2: MAPA 'mapa1.txt' (Fase 4-5)
============================================================
Mapa original:
S....
.##..
...#.
.#..G

Inicio: (0, 0) | Meta: (3, 4) | Casillas libres: 16

--- BFS ---
Longitud del camino: 8
Nodos explorados: 16
S....
*##..
***#.
.#**G

--- DFS ---
Longitud del camino: 8
Nodos explorados: 8
S****
.##.*
...#*
.#..G

--- A* ---
Longitud del camino: 8
Costo total: 7
Nodos explorados: 16
S....
*##..
***#.
.#**G

--- Comparacion en 'mapa1.txt' ---
Algoritmo Longitud camino   Nodos explorados  
BFS       8                 16                
DFS       8                 8                 
A*        8                 16                

============================================================
PARTE 2: MAPA 'mapa2.txt' (Fase 4-5)
============================================================
Mapa original:
S..........
#########.#
...........
.##########
...........
#########.#
...........
.##########
...........
#########.#
..........G

Inicio: (0, 0) | Meta: (10, 10) | Casillas libres: 71

--- BFS ---
Longitud del camino: 57
Nodos explorados: 63
S*********.
#########*#
**********.
*##########
**********.
#########*#
**********.
*##########
**********.
#########*#
.........*G

--- DFS ---
Longitud del camino: 57
Nodos explorados: 62
S*********.
#########*#
**********.
*##########
**********.
#########*#
**********.
*##########
**********.
#########*#
.........*G

--- A* ---
Longitud del camino: 57
Costo total: 56
Nodos explorados: 62
S*********.
#########*#
**********.
*##########
**********.
#########*#
**********.
*##########
**********.
#########*#
.........*G

--- Comparacion en 'mapa2.txt' ---
Algoritmo Longitud camino   Nodos explorados  
BFS       57                63                
DFS       57                62                
A*        57                62                
