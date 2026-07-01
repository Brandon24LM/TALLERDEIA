"""
mapas.py
Lectura de mapas de cuadricula en formato de texto y calculo de vecinos.
"""


def leer_mapa(mapa_texto):
    """
    Convierte una lista de strings en:
      - libres: set de coordenadas (fila, col) que NO son obstaculo
      - inicio: coordenada de 'S'
      - meta: coordenada de 'G'
    """
    inicio = None
    meta = None
    libres = set()

    for f, fila in enumerate(mapa_texto):
        for c, celda in enumerate(fila):
            if celda == "#":
                continue  # obstaculo: no se agrega a libres
            libres.add((f, c))
            if celda == "S":
                inicio = (f, c)
            elif celda == "G":
                meta = (f, c)

    if inicio is None or meta is None:
        raise ValueError("El mapa debe tener exactamente un 'S' y un 'G'.")

    return libres, inicio, meta


def vecinos_grid(nodo, libres):
    """Vecinos ortogonales (arriba, abajo, izquierda, derecha) dentro de libres."""
    f, c = nodo
    candidatos = [(f - 1, c), (f + 1, c), (f, c - 1), (f, c + 1)]
    return [n for n in candidatos if n in libres]


def imprimir_mapa_con_camino(mapa_texto, camino):
    """Imprime el mapa marcando el camino encontrado con '*'."""
    camino_set = set(camino) if camino else set()
    filas = [list(fila) for fila in mapa_texto]

    for (f, c) in camino_set:
        if filas[f][c] not in ("S", "G"):
            filas[f][c] = "*"

    for fila in filas:
        print("".join(fila))
