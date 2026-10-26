# Tarea Barcos - Diseño de Algoritmos

Trabajo práctico de la materia **Diseño de Algoritmos** (6to Semestre).

El proyecto simula la logística y distribución de carga marítima en **barcos de puerto a puerto**, utilizando los métodos vistos en clase:

---

## 📌 Métodos Utilizados

1. **Problema de la Mochila (Knapsack 0/1):**
   - Utilizado para optimizar la carga del barco respetando las restricciones de peso (kg) y volumen (m³).
   - Aplica programación dinámica con la matriz `dp[i][w]` para maximizar la prioridad y valor de las cargas transportadas.

2. **Algoritmo de Dijkstra:**
   - Calcula la ruta marítima más corta en distancia náutica (km) y tiempo estimado de navegación entre puertos internacionales y colombianos.
   - Usa una cola de prioridad (`heapq`).

3. **Árbol Binario de Búsqueda (BST):**
   - Organiza los paquetes en la bodega portuaria ordenados por su ID para búsquedas rápidas en $\mathcal{O}(\log n)$.

4. **Exportación a Excel:**
   - Genera el archivo `reporte_logistica_barcos.xlsx` con los datos de las cargas, el llenado del barco y las rutas entre puertos calculadas.

---

## 🚀 Cómo Ejecutar

En la terminal de Visual Studio Code:

```bash
python main.py
```

Opciones del menú:
1. Ver inventario de bodega (BST)
2. Llenar barco (Mochila)
3. Calcular rutas entre puertos (Dijkstra)
4. Generar Excel
5. Ejecutar todo
0. Salir

---

## 📁 Archivos del Proyecto

- `main.py`: Menú principal del programa.
- `algoritmos/`:
  - `mochila.py`: Algoritmo de la mochila 0/1 (programación dinámica y greedy).
  - `dijkstra.py`: Algoritmo de Dijkstra con cola de prioridad.
  - `arbol_bodega.py`: Árbol binario de búsqueda (BST) para la bodega.
- `modelos/`:
  - `paquete.py`: Clase Paquete con dimensiones (alto, ancho, profundidad), volumen, peso y destino portuario (lat, lon).
  - `transporte.py`: Clase `BarcoCarga` con capacidad de peso y volumen.
- `red_logistica/`:
  - `grafo_rutas.py`: Grafo con las coordenadas y conexiones marítimas entre puertos.
- `exportador/`:
  - `exportar_excel.py`: Genera el archivo `.xlsx` con `openpyxl`.
- `data/`:
  - `paquetes_ejemplo.json`: Cargas marítimas de prueba entre puertos.
- `reporte_logistica_barcos.xlsx`: Archivo Excel con los resultados.
