# Reflexión final

Durante el desarrollo del taller, BFS resultó el algoritmo más fácil
de depurar. Su lógica es lineal: se saca un nodo de la cola, se revisa
si es la meta y se agregan los vecinos no visitados. Al imprimir la
frontera en cada paso, era evidente cuándo algo fallaba, porque los
nodos aparecían y desaparecían en el orden esperado. DFS, en cambio,
generó más confusión al inicio, ya que al usar una pila el camino
podía "irse" por una rama larga antes de retroceder, y no siempre era
obvio si el algoritmo seguía avanzando o estaba atascado.

El error más frecuente durante la implementación fue marcar los nodos
como visitados demasiado tarde, justo el problema señalado en el
material del taller. Esto provocaba que un mismo nodo se agregara
varias veces a la frontera, lo cual no siempre rompía el resultado
final, pero sí hacía que el algoritmo revisara nodos de más, lo cual
se notó al comparar la cantidad de pasos entre ejecuciones.

En cuanto a cuándo usar cada algoritmo: BFS es la mejor opción cuando
se necesita garantizar el camino más corto y todos los movimientos
cuestan lo mismo. DFS es útil cuando solo interesa saber si existe
algún camino, o para explorar estructuras muy profundas con poca
memoria. A* es la opción preferida cuando se dispone de una buena
heurística, porque combina la garantía de optimalidad de BFS con una
exploración más dirigida hacia la meta, evitando revisar nodos
irrelevantes.
