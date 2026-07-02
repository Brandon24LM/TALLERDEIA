# Reflexión final

> Nota: este es un borrador editable. Ajusten el contenido según lo que
> realmente experimentó su equipo durante el taller antes de entregarlo.

Durante este taller implementamos BFS, DFS y A* tanto para un grafo simple
como para mapas de cuadrícula, y esto nos permitió comparar de forma directa
sus diferencias.

El algoritmo más fácil de depurar fue BFS. Al usar una cola, el orden de
exploración es predecible: siempre se revisan primero los nodos más cercanos
al inicio, así que las trazas de frontera y visitados eran fáciles de seguir
y de anticipar. DFS, en cambio, fue más difícil de seguir mentalmente porque
la pila hace que el algoritmo "salte" de una rama a otra muy rápido, y a
veces encontramos caminos mucho más largos de lo esperado.

El error que apareció con más frecuencia fue marcar los nodos como visitados
demasiado tarde, justo el problema que se advertía en la guía. Esto provocaba
que un mismo nodo entrara varias veces a la frontera o a la pila, lo cual no
siempre producía un error visible, pero sí resultados incorrectos o caminos
más largos de lo necesario. Aprendimos que ese tipo de fallas silenciosas son
las más peligrosas porque el programa "funciona" sin avisar que algo está mal.

En cuanto a cuándo usar cada algoritmo: usaríamos BFS cuando todos los
movimientos cuestan lo mismo y necesitamos el camino más corto garantizado;
DFS cuando solo nos interesa saber si existe algún camino, sin importar su
longitud, o para explorar todo el espacio de búsqueda; y A* cuando el mapa es
grande y queremos encontrar el camino óptimo de forma más eficiente que BFS,
aprovechando una heurística que guíe la búsqueda hacia la meta.
