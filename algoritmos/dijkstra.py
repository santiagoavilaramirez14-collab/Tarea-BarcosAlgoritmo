# Algoritmo de Dijkstra con cola de prioridad (heapq)
# para encontrar la ruta mas corta y tiempos de entrega

import heapq

def dijkstra(grafo, inicio):
    """
    Encuentra la distancia mínima desde 'inicio' a todos los demás nodos
    del grafo ponderado usando una cola de prioridad min-heap (heapq).
    
    Complejidad: O((V + E) log V)
    
    Estructura del grafo:
      dict: { 'NodoA': [('NodoB', peso, modalidad, tiempo_h), ...] }
    """
    # Inicializar todas las distancias en infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    tiempos = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    detalles_arista = {nodo: None for nodo in grafo}
    
    distancias[inicio] = 0
    tiempos[inicio] = 0.0
    
    # Heap de prioridad: tuplas de (distancia_acumulada, nodo_actual)
    heap = [(0, inicio)]
    
    while heap:
        dist_actual, nodo_actual = heapq.heappop(heap)
        
        # Si encontramos una distancia mayor que la ya registrada, la descartamos
        if dist_actual > distancias[nodo_actual]:
            continue
            
        # Explorar vecinos
        for conexion in grafo.get(nodo_actual, []):
            # Soporta tanto tuplas de 2 elementos (vecino, peso) como de 4 (vecino, peso, modo, tiempo)
            if len(conexion) == 2:
                vecino, peso = conexion
                modo, tiempo = "terrestre", peso / 50.0
            else:
                vecino, peso, modo, tiempo = conexion
                
            nueva_dist = dist_actual + peso
            nuevo_tiempo = tiempos[nodo_actual] + tiempo
            
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = round(nueva_dist, 2)
                tiempos[vecino] = round(nuevo_tiempo, 2)
                predecesores[vecino] = nodo_actual
                detalles_arista[vecino] = {"modo": modo, "distancia_km": peso, "tiempo_h": tiempo}
                heapq.heappush(heap, (nueva_dist, vecino))
                
    return distancias, tiempos, predecesores, detalles_arista


def reconstruir_ruta(predecesores, detalles_arista, inicio, fin):
    """
    Reconstruye el camino óptimo desde 'inicio' hasta 'fin' a partir
    del diccionario de predecesores devuelto por Dijkstra.
    
    Retorna:
      - ruta: lista de nombres de nodos en orden cronológico
      - tramos: lista de diccionarios con el detalle de cada tramo (origen, destino, modo, km, horas)
    """
    if fin not in predecesores or (fin != inicio and predecesores[fin] is None):
        return None, []
        
    ruta = []
    tramos = []
    actual = fin
    
    while actual is not None:
        ruta.append(actual)
        anterior = predecesores[actual]
        if anterior is not None and detalles_arista.get(actual):
            info = detalles_arista[actual]
            tramos.append({
                "desde": anterior,
                "hasta": actual,
                "modo": info["modo"],
                "distancia_km": info["distancia_km"],
                "tiempo_h": info["tiempo_h"]
            })
        actual = anterior
        
    ruta.reverse()
    tramos.reverse()
    return ruta, tramos
