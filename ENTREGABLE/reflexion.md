# Reflexión final

De los tres algoritmos, **BFS fue el más fácil de depurar**. Su
comportamiento es predecible: la frontera crece de forma ordenada, nivel por
nivel, así que cualquier anomalía (por ejemplo, un nodo repetido en la cola)
se nota casi de inmediato al imprimir las trazas. DFS fue más difícil de
seguir porque la pila cambia de "rama" constantemente y el camino que
devuelve no siempre es intuitivo a simple vista. A* fue el más complejo de
depurar, no porque el código sea más largo, sino porque hay más variables en
juego a la vez (costo acumulado, heurística y valor f), y un error en
cualquiera de ellas puede producir un camino que *parece* correcto pero no es
el óptimo.

El error que apareció con más frecuencia durante el desarrollo fue
exactamente el mencionado en la Fase 2: **marcar un nodo como visitado
demasiado tarde**, lo que provocaba que el mismo nodo entrara varias veces a
la cola o a la pila. Es un error silencioso: el algoritmo sigue devolviendo
un resultado, solo que explora más nodos de los necesarios, y eso solo se
detecta comparando la cantidad de nodos explorados entre ejecuciones.

En cuanto a cuándo usar cada uno: **BFS** es la mejor opción cuando se
necesita garantizar el camino más corto en un grafo sin pesos, como en
nuestro mapa de laberinto. **DFS** conviene cuando solo interesa saber si
existe algún camino (no necesariamente el más corto), o para explorar
estructuras como árboles de decisión. **A\*** es la mejor opción cuando el
mapa es grande y se dispone de una buena heurística, porque llega al mismo
resultado óptimo que BFS explorando normalmente menos nodos.
