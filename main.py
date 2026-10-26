# Tarea Barcos - Diseno de Algoritmos
# Optimizacion de Carga en Barcos (Mochila) y Rutas entre Puertos (Dijkstra)

import os
import sys
import json
from pathlib import Path

# Configurar rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from modelos.paquete import Paquete
from modelos.transporte import BarcoCarga
from algoritmos.mochila import optimizar_mochila_dp, optimizar_mochila_greedy, asignar_carga_a_vehiculo
from algoritmos.dijkstra import dijkstra, reconstruir_ruta
from algoritmos.arbol_bodega import ArbolBodega
from red_logistica.grafo_rutas import RedMaritimaPuertos
from exportador.exportar_excel import generar_reporte_excel


def cargar_paquetes(ruta_json=None):
    """Carga los paquetes y cargas de prueba desde el archivo JSON"""
    if ruta_json is None:
        ruta_json = BASE_DIR / "data" / "paquetes_ejemplo.json"
        
    with open(ruta_json, "r", encoding="utf-8") as f:
        datos = json.load(f)
        
    paquetes = []
    for item in datos:
        p = Paquete(
            id_paquete=item["id_paquete"],
            descripcion=item["descripcion"],
            alto=item["alto"],
            ancho=item["ancho"],
            profundidad=item["profundidad"],
            peso_kg=item["peso_kg"],
            origen=item["origen"],
            destino_nombre=item["destino_nombre"],
            lat=item["lat"],
            lon=item["lon"],
            modalidad_preferida="barco",
            prioridad=item["prioridad"]
        )
        paquetes.append(p)
    return paquetes


def ejecutar_optimizacion_mochila(paquetes):
    """
    Aplica el algoritmo de la Mochila 0/1 para llenar el barco de carga
    optimizando el espacio (volumen) y el peso segun la prioridad de cada carga.
    """
    barco = BarcoCarga("BAR-01", "Barco Portacontenedores", capacidad_peso_kg=25000, capacidad_volumen_m3=180)
    asignar_carga_a_vehiculo(barco, paquetes)
    return [barco]


def calcular_rutas_dijkstra(paquetes, red):
    """
    Aplica Dijkstra para calcular la ruta maritima mas corta y el tiempo estimado
    entre los puertos de origen y destino de cada paquete.
    """
    rutas_calculadas = []
    
    for p in paquetes:
        distancias, tiempos, predecesores, detalles = dijkstra(red.grafo, p.origen)
        camino, tramos = reconstruir_ruta(predecesores, detalles, p.origen, p.destino_nombre)
        
        dist_total = distancias.get(p.destino_nombre, float('inf'))
        tiempo_total = tiempos.get(p.destino_nombre, float('inf'))
        
        rutas_calculadas.append({
            "id_paquete": p.id_paquete,
            "descripcion": p.descripcion,
            "origen": p.origen,
            "destino": p.destino_nombre,
            "ruta": camino,
            "tramos": tramos,
            "distancia_km": dist_total if dist_total != float('inf') else 0,
            "tiempo_h": tiempo_total if tiempo_total != float('inf') else 0
        })
        
    return rutas_calculadas


def mostrar_menu():
    print("\n" + "=" * 45)
    print("      SISTEMA DE RUTAS Y BARCOS")
    print("=" * 45)
    print("1. Ver inventario de bodega (BST)")
    print("2. Llenar barco (Mochila)")
    print("3. Calcular rutas entre puertos (Dijkstra)")
    print("4. Generar Excel")
    print("5. Ejecutar todo")
    print("0. Salir")
    print("=" * 45)


def main():
    paquetes = cargar_paquetes()
    red = RedMaritimaPuertos()

    # Cargar bodega local con el arbol BST
    bodega = ArbolBodega()
    for p in paquetes:
        bodega.insertar(p)

    vehiculos_optimizados = None
    rutas_calculadas = None

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (0-5): ").strip()

        if opcion == "1":
            print("\n--- PAQUETES EN BODEGA (INORDEN BST) ---")
            print(f"{'ID':<6} | {'Descripcion':<35} | {'Vol (m3)':<10} | {'Peso (kg)':<10} | {'Destino':<35}")
            print("-" * 110)
            for p in bodega.inorden():
                print(f"{p.id_paquete:<6} | {p.descripcion[:33]:<35} | {p.volumen_m3:<10} | {p.peso_kg:<10} | {p.destino_nombre[:33]:<35}")

        elif opcion == "2":
            print("\n--- ASIGNACION DE CARGA AL BARCO (MOCHILA 0/1) ---")
            vehiculos_optimizados = ejecutar_optimizacion_mochila(paquetes)
            barco = vehiculos_optimizados[0]
            print(f"\n{barco.nombre} [BARCO]:")
            print(f"   Peso cargado: {barco.peso_actual_kg} / {barco.capacidad_peso_kg} kg ({barco.porcentaje_peso_usado}%)")
            print(f"   Volumen cargado: {barco.volumen_actual_m3} / {barco.capacidad_volumen_m3} m3 ({barco.porcentaje_volumen_usado}%)")
            print(f"   Paquetes asignados ({len(barco.paquetes_asignados)}): {[p.id_paquete for p in barco.paquetes_asignados]}")

        elif opcion == "3":
            print("\n--- RUTAS MARITIMAS OPTIMAS (DIJKSTRA) ---")
            rutas_calculadas = calcular_rutas_dijkstra(paquetes, red)
            for r in rutas_calculadas:
                camino = " -> ".join(r["ruta"]) if r["ruta"] else "Sin ruta"
                print(f"\nPaquete #{r['id_paquete']} ({r['descripcion']}):")
                print(f"   Puerto Origen: {r['origen']}")
                print(f"   Puerto Destino: {r['destino']}")
                print(f"   Distancia nautica: {r['distancia_km']} km")
                print(f"   Tiempo estimado de navegacion: {r['tiempo_h']} horas")
                print(f"   Ruta: {camino}")

        elif opcion == "4":
            print("\n--- GENERANDO EXCEL ---")
            if vehiculos_optimizados is None:
                vehiculos_optimizados = ejecutar_optimizacion_mochila(paquetes)
            if rutas_calculadas is None:
                rutas_calculadas = calcular_rutas_dijkstra(paquetes, red)

            kpis = {
                "total_paquetes": len(paquetes),
                "peso_total_kg": sum(p.peso_kg for p in paquetes),
                "volumen_total_m3": sum(p.volumen_m3 for p in paquetes),
                "aprovechamiento_promedio": vehiculos_optimizados[0].porcentaje_volumen_usado
            }

            excel_path = BASE_DIR / "reporte_logistica_barcos.xlsx"
            generar_reporte_excel(str(excel_path), paquetes, vehiculos_optimizados, rutas_calculadas, kpis)
            print(f"Reporte generado: {excel_path.name}")

        elif opcion == "5":
            print("\n--- EJECUTANDO FLUJO COMPLETO ---")
            vehiculos_optimizados = ejecutar_optimizacion_mochila(paquetes)
            rutas_calculadas = calcular_rutas_dijkstra(paquetes, red)

            kpis = {
                "total_paquetes": len(paquetes),
                "peso_total_kg": sum(p.peso_kg for p in paquetes),
                "volumen_total_m3": sum(p.volumen_m3 for p in paquetes),
                "aprovechamiento_promedio": vehiculos_optimizados[0].porcentaje_volumen_usado
            }
            excel_path = BASE_DIR / "reporte_logistica_barcos.xlsx"
            generar_reporte_excel(str(excel_path), paquetes, vehiculos_optimizados, rutas_calculadas, kpis)
            print("Listo. Archivo Excel generado correctamente.")

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
