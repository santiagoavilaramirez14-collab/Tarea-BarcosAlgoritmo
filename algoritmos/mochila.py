"""
====================================================================
ALGORITMO DE LA MOCHILA (KNAPSACK) - PROGRAMACIÓN DINÁMICA & GREEDY
Visto en Sesiones 8, 9 y 10: Algoritmos Ávidos y Programación Dinámica
====================================================================
"""

def optimizar_mochila_dp(paquetes, capacidad_peso, capacidad_volumen=None, factor_escala_peso=1):
    """
    Algoritmo de la Mochila 0/1 usando Programación Dinámica (Bottom-Up con Tabulación).
    
    Recurrencia vista en clase:
      si peso[i] > w:
          dp[i][w] = dp[i-1][w]
      si no:
          dp[i][w] = max(dp[i-1][w], valor[i] + dp[i-1][w - peso[i]])
          
    Parámetros:
      - paquetes: lista de instancias de Paquete
      - capacidad_peso: capacidad máxima en kg (entero o discretizado)
      - capacidad_volumen: capacidad máxima volumétrica (opcional para control secundario)
      
    Retorna:
      - valor_optimo: ganancia / valor total óptimo alcanzado
      - seleccionados: lista de paquetes elegidos
      - tabla_dp: matriz de programación dinámica construida
    """
    n = len(paquetes)
    # Convertimos capacidades a enteros para la matriz DP
    W = int(capacidad_peso * factor_escala_peso)
    
    # Matriz DP de dimensiones (n + 1) x (W + 1)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Llenado de la tabla (Bottom-Up)
    for i in range(1, n + 1):
        paq = paquetes[i - 1]
        peso_i = int(paq.peso_kg * factor_escala_peso)
        valor_i = paq.prioridad  # Se maximiza la prioridad / importancia de entrega
        
        for w in range(W + 1):
            if peso_i > w:
                dp[i][w] = dp[i - 1][w]
            else:
                opcion_sin_paquete = dp[i - 1][w]
                opcion_con_paquete = valor_i + dp[i - 1][w - peso_i]
                dp[i][w] = max(opcion_sin_paquete, opcion_con_paquete)
                
    # Reconstrucción de la solución (Backtracking sobre la tabla DP)
    seleccionados = []
    w_restante = W
    volumen_acumulado = 0.0
    
    for i in range(n, 0, -1):
        if dp[i][w_restante] != dp[i - 1][w_restante]:
            paq = paquetes[i - 1]
            # Si hay restricción volumétrica secundaria, verificamos que no la sobrepase
            if capacidad_volumen is None or (volumen_acumulado + paq.volumen_m3 <= capacidad_volumen):
                seleccionados.append(paq)
                w_restante -= int(paq.peso_kg * factor_escala_peso)
                volumen_acumulado += paq.volumen_m3
                
    seleccionados.reverse()
    valor_optimo = sum(p.prioridad for p in seleccionados)
    return valor_optimo, seleccionados, dp


def optimizar_mochila_greedy(paquetes, capacidad_peso, capacidad_volumen=float('inf')):
    """
    Algoritmo Ávido / Greedy para la Mochila (visto en Sesión 8).
    Estrategia: Ordenar los paquetes por su densidad de valor (prioridad / peso)
    y tomar la mejor opción local en cada paso mientras haya espacio disponible.
    
    Sirve para comparar el resultado Greedy vs el resultado exacto de Programación Dinámica.
    """
    # Ordenar de mayor a menor según ratio (prioridad / peso)
    paquetes_ordenados = sorted(
        paquetes, 
        key=lambda p: (p.prioridad / max(p.peso_kg, 0.1), p.prioridad / max(p.volumen_m3, 0.01)), 
        reverse=True
    )
    
    seleccionados = []
    peso_actual = 0.0
    volumen_actual = 0.0
    valor_total = 0
    
    for p in paquetes_ordenados:
        if (peso_actual + p.peso_kg <= capacidad_peso) and (volumen_actual + p.volumen_m3 <= capacidad_volumen):
            seleccionados.append(p)
            peso_actual += p.peso_kg
            volumen_actual += p.volumen_m3
            valor_total += p.prioridad
            
    return valor_total, seleccionados, round(peso_actual, 2), round(volumen_actual, 3)


def asignar_carga_a_vehiculo(vehiculo, paquetes_candidatos):
    """
    Aplica el algoritmo de la mochila para llenar óptimamente un vehículo específico
    (Barco, Avión, Furgón, Van, Moto), respetando tanto límite de peso como de volumen.
    """
    # Usamos la estrategia combinada DP + filtro de volumen
    _, seleccionados, _ = optimizar_mochila_dp(
        paquetes_candidatos, 
        capacidad_peso=vehiculo.capacidad_peso_kg,
        capacidad_volumen=vehiculo.capacidad_volumen_m3
    )
    
    vehiculo.vaciar_carga()
    no_asignados = []
    
    for p in paquetes_candidatos:
        if p in seleccionados and vehiculo.puede_cargar(p):
            vehiculo.cargar_paquete(p)
        else:
            no_asignados.append(p)
            
    return vehiculo, no_asignados
