# Taller completo: BFS, DFS y A\* en Python

## 1. Situación problema

Un robot debe moverse dentro de un mapa para encontrar una ruta desde un punto inicial hasta una meta. Algunas casillas están bloqueadas por obstáculos. El robot no puede atravesarlas. Solo puede moverse arriba, abajo, izquierda y derecha.

El reto consiste en programar tres estrategias de búsqueda:

- **BFS**, para encontrar el camino más corto cuando todos los movimientos cuestan lo mismo.
- **DFS**, para explorar rutas en profundidad, aunque no siempre encuentre la ruta más corta.
- **A\***, para buscar de manera más inteligente usando una heurística.

## 2. Conceptos básicos

### ¿Qué es un grafo?

Un grafo es una estructura formada por nodos y conexiones. En un mapa, cada casilla libre puede verse como un nodo y cada movimiento permitido como una conexión.

### ¿Qué es un nodo?

Un nodo representa un estado posible. En un mapa, un nodo puede ser una coordenada como `(2, 3)`.

### ¿Qué es una frontera?

La frontera es la lista de lugares que el algoritmo todavía debe explorar. Es como una fila de tareas pendientes, porque aparentemente hasta los algoritmos tienen una lista de cosas por hacer.

### ¿Qué es un conjunto de visitados?

Es el registro de nodos que ya fueron revisados. Evita que el algoritmo dé vueltas infinitas.

### ¿Qué es reconstruir el camino?

Cuando el algoritmo encuentra la meta, necesita regresar desde la meta hasta el inicio usando un diccionario de padres. Ese diccionario guarda de dónde vino cada nodo.

---

## 3. Fase 1: representar un grafo simple

Antes de trabajar con mapas, se recomienda iniciar con un grafo pequeño.

```python
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
```

### Preguntas de análisis

1. ¿Cuáles son los vecinos de `A`?
2. ¿Qué nodos no tienen salida?
3. ¿Qué rutas posibles existen desde `A` hasta `F`?

---

## 4. Fase 2: implementar BFS de forma incremental

### Objetivo

Crear una función que encuentre el camino más corto en un grafo sin pesos.

### Idea

BFS usa una cola. Primero explora los nodos más cercanos al inicio.

### Pasos

1. Crear una cola con el nodo inicial.
2. Crear un conjunto de visitados.
3. Crear un diccionario de padres.
4. Mientras la cola no esté vacía:
   - sacar el primer nodo;
   - revisar si es la meta;
   - agregar vecinos no visitados;
   - guardar el padre de cada vecino.
5. Si se encuentra la meta, reconstruir el camino.

### Error frecuente

Marcar un nodo como visitado demasiado tarde. Eso puede hacer que el mismo nodo entre varias veces en la cola. El algoritmo sigue funcionando a veces, que es la peor clase de error: el que parece inocente y después arruina todo en silencio.

---

## 5. Fase 3: implementar DFS de forma incremental

### Objetivo

Crear una función que explore caminos en profundidad.

### Idea

DFS usa una pila. Explora una ruta hasta donde pueda y luego retrocede.

### Pasos

1. Crear una pila con el nodo inicial.
2. Crear un conjunto de visitados.
3. Crear un diccionario de padres.
4. Mientras la pila no esté vacía:
   - sacar el último nodo;
   - revisar si es la meta;
   - agregar vecinos no visitados;
   - guardar el padre de cada vecino.
5. Reconstruir el camino si se encuentra la meta.

### Diferencia clave con BFS

BFS usa cola: primero entra, primero sale.

DFS usa pila: último en entrar, primero en salir.

---

## 6. Fase 4: trabajar con mapas de cuadrícula

Un mapa puede representarse con texto:

```text
S....
.##..
...#.
.#..G
```

Significado:

| Símbolo | Significado |
|---|---|
| `S` | Inicio |
| `G` | Meta |
| `.` | Camino libre |
| `#` | Obstáculo |

Cada casilla libre se representa como una coordenada `(fila, columna)`.

---

## 7. Fase 5: implementar A\*

### Objetivo

Encontrar una ruta eficiente usando costo acumulado y una estimación hacia la meta.

### Fórmula principal

```text
f(n) = g(n) + h(n)
```

Donde:

- `g(n)` es el costo desde el inicio hasta el nodo actual.
- `h(n)` es la estimación desde el nodo actual hasta la meta.
- `f(n)` es el valor usado para priorizar qué nodo explorar.

### Heurística Manhattan

Para movimientos arriba, abajo, izquierda y derecha, se puede usar distancia Manhattan:

```python
abs(fila_actual - fila_meta) + abs(col_actual - col_meta)
```

### Pasos de A\*

1. Crear una cola de prioridad.
2. Guardar el costo acumulado desde el inicio.
3. Guardar el padre de cada nodo.
4. Extraer siempre el nodo con menor `f(n)`.
5. Revisar vecinos válidos.
6. Actualizar costos si se encuentra una mejor ruta.
7. Reconstruir el camino al llegar a la meta.

---

## 8. Depuración incremental

### Regla principal

No depures todo el algoritmo completo al final. Depura por capas.

### Capas recomendadas

1. Verificar que el mapa se lee correctamente.
2. Verificar que el inicio y la meta existen.
3. Verificar que los vecinos se calculan bien.
4. Verificar que la frontera crece y disminuye correctamente.
5. Verificar que los visitados no se repiten.
6. Verificar que los padres se guardan bien.
7. Verificar que el camino reconstruido inicia en `S` y termina en `G`.
8. Verificar el resultado con un mapa pequeño.

---

## 9. Actividad guiada en clase

### Parte A: comprensión

Responde:

1. ¿Por qué BFS encuentra el camino más corto en grafos sin pesos?
2. ¿Por qué DFS puede encontrar una ruta más larga?
3. ¿Qué ventaja tiene A\* frente a BFS?
4. ¿Qué ocurre si la heurística sobreestima el costo real?
5. ¿Por qué es útil imprimir la frontera durante la depuración?

### Parte B: programación

Implementa y prueba:

1. BFS en grafo.
2. DFS en grafo.
3. BFS en mapa.
4. A\* en mapa.
5. Comparación entre resultados.

### Parte C: depuración

Agrega trazas para mostrar:

- nodo actual;
- frontera;
- visitados;
- vecinos válidos;
- padre asignado;
- costo acumulado en A\*.

---

## 10. Entregable final

Cada equipo debe entregar un repositorio GitHub con:

1. Código funcional de BFS, DFS y A\*.
2. Al menos dos mapas de prueba.
3. Captura o salida de consola mostrando resultados.
4. Archivo `README.md` explicando cómo ejecutar.
5. Reflexión final de 150 a 250 palabras:
   - ¿Qué algoritmo fue más fácil de depurar?
   - ¿Qué error apareció con mayor frecuencia?
   - ¿En qué caso usarían BFS, DFS o A\*?

