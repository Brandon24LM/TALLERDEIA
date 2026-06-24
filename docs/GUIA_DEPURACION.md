# Guía de depuración incremental

## ¿Qué significa depurar incrementalmente?

Significa revisar el programa por partes pequeñas, no cuando todo está terminado y ya se convirtió en una criatura triste e incomprensible.

## Lista de verificación

### 1. Entrada de datos

- ¿El grafo existe?
- ¿El mapa se carga correctamente?
- ¿Todas las filas del mapa tienen el mismo tamaño?
- ¿Existe `S`?
- ¿Existe `G`?

### 2. Vecinos

- ¿El algoritmo genera vecinos dentro del mapa?
- ¿Evita obstáculos?
- ¿Evita posiciones negativas?
- ¿Evita salirse por la derecha o por abajo?

### 3. Frontera

- En BFS, ¿la frontera funciona como cola?
- En DFS, ¿la frontera funciona como pila?
- En A*, ¿la frontera usa prioridad?

### 4. Visitados

- ¿El inicio se marca como visitado?
- ¿Cada nodo entra una sola vez cuando corresponde?
- ¿Se evitan ciclos?

### 5. Padres

- ¿Cada vecino guarda correctamente desde dónde llegó?
- ¿El inicio tiene padre `None`?
- ¿La meta aparece en el diccionario de padres?

### 6. Camino final

- ¿El camino inicia en `S`?
- ¿El camino termina en `G`?
- ¿El camino no atraviesa obstáculos?
- ¿El camino se puede dibujar sobre el mapa?

## Trazas sugeridas

Agrega impresiones como estas:

```python
print("Actual:", current)
print("Frontera:", frontier)
print("Visitados:", visited)
print("Vecino:", neighbor)
print("Padre asignado:", came_from[neighbor])
```

## Errores frecuentes

| Error | Síntoma | Solución |
|---|---|---|
| No marcar visitados | El algoritmo se repite | Marcar al agregar a la frontera |
| Invertir pila y cola | BFS actúa como DFS | Revisar `popleft()` y `pop()` |
| No guardar padres | No se puede reconstruir camino | Guardar `came_from[vecino] = actual` |
| Heurística mal calculada | A* explora raro | Revisar distancia Manhattan |
| Mapa irregular | Error de índice | Validar ancho de filas |

