# Tarea Barcos - Diseño de Algoritmos

Trabajo práctico de la materia **Diseño de Algoritmos** (6to Semestre).

El proyecto simula un sistema de distribución de paquetes que combina transporte en **aviones** (país a país), **barcos** (puerto a puerto) y transporte **terrestre** en Ibagué (furgones, vans y motos).

---

## 📌 Métodos Utilizados

1. **Problema de la Mochila (Knapsack 0/1):**
   - Utilizado para optimizar el espacio y el peso en cada medio de transporte.
   - Aplica programación dinámica con la tabla `dp[i][w]` para seleccionar la combinación óptima de paquetes según su peso y volumen.

2. **Algoritmo de Dijkstra:**
   - Utilizado para calcular la ruta más corta desde el origen (puerto o aeropuerto) hasta el destino en Ibagué (Centro, El Salado, Picaleña, Mirolindo, Ricaurte).
   - Usa una cola de prioridad (`heapq`) para calcular la menor distancia en kilómetros y el tiempo aproximado de viaje.

3. **Árbol Binario de Búsqueda (BST):**
   - Organiza los paquetes en la bodega local ordenados por su ID para búsquedas rápidas.

4. **Exportación a Excel:**
   - Genera el archivo `reporte_logistica_barcos.xlsx` con el inventario de paquetes, asignación de carga y las rutas calculadas.

5. **Simulación en Mapa:**
   - Simula las rutas marítimas entre puertos (Shanghái, Rotterdam, Los Ángeles, Miami, Buenaventura, Cartagena, Barranquilla, Santa Marta) y la entrega en Ibagué.

---

## 🚀 Cómo Ejecutar

En la terminal de Visual Studio Code:

```bash
python main.py
```

Opciones del menú:
1. Ver inventario de bodega (BST)
2. Llenar vehículos (Mochila)
3. Calcular rutas (Dijkstra)
4. Generar Excel
5. Ver mapa interactivo
6. Ejecutar todo
0. Salir

---

## 📁 Archivos del Proyecto

- `main.py`: Menú principal del programa.
- `algoritmos/`:
  - `mochila.py`: Algoritmo de la mochila 0/1 (programación dinámica y greedy).
  - `dijkstra.py`: Algoritmo de Dijkstra con cola de prioridad.
  - `arbol_bodega.py`: Árbol binario de búsqueda (BST) para la bodega.
- `modelos/`:
  - `paquete.py`: Clase Paquete con dimensiones (alto, ancho, profundidad), volumen, peso y destino (lat, lon).
  - `transporte.py`: Clases para barco, avión, furgón, van y moto con sus capacidades.
- `red_logistica/`:
  - `grafo_rutas.py`: Grafo con las coordenadas y conexiones entre puertos, aeropuertos y barrios de Ibagué.
- `exportador/`:
  - `exportar_excel.py`: Genera el archivo `.xlsx` con `openpyxl`.
- `visualizacion/`:
  - `simulador_mapa.html`: Mapa interactivo con Leaflet.
- `data/`:
  - `paquetes_ejemplo.json`: Datos de prueba de los paquetes.
- `reporte_logistica_barcos.xlsx`: Archivo Excel con los resultados.
