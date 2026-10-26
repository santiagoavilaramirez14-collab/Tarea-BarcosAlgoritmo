# Sistema Logístico Intermodal: Barcos, Dijkstra y Mochila 🚢📦

**Asignatura:** Diseño de Algoritmos — 6to Semestre  
**Universidad:** Corporación Universitaria Minuto de Dios (UNIMINUTO)  
**Tema:** Trabajo / Parcial Práctico: Optimización Multimodal (Barcos, Aviones, Terrestre Ibagué)  
**Docente:** Diseño de Algoritmos  
**Estudiante:** Santiago Ramírez  

---

## 📌 1. Descripción del Proyecto

Este proyecto resuelve de forma integral la logística de distribución de carga a nivel internacional y local, abarcando tres niveles de transporte intermodal:
1. **Aviones (Carga País a País):** Transporte aéreo de alta velocidad para cargas prioritarias, urgentes o médicas (Shanghái, Ámsterdam, Miami hacia Bogotá El Dorado).
2. **Barcos (Carga Puerto a Puerto):** Transporte marítimo masivo de contenedores y maquinaria pesada entre puertos internacionales (Shanghái, Rotterdam, Los Ángeles, Miami) y puertos marítimos colombianos (Buenaventura en el Pacífico; Cartagena, Barranquilla y Santa Marta en el Caribe).
3. **Transporte Terrestre (Distribución en Ibagué y Enlace Nacional):** Recepción de la carga en el Hub Logístico de Ibagué (Tolima) y distribución de última milla a través de tres tipos de vehículos especializados:
   - **Furgones:** Para cargas pesadas e industriales hacia el Parque Industrial de Picaleña (Comuna 9).
   - **Vans:** Para paquetes comerciales y residenciales hacia El Salado (Comuna 7) y Mirolindo.
   - **Motos:** Para mensajería rápida, documentos y paquetería ligera hacia la Zona Centro (Comuna 1) y Ricaurte (Comuna 12).

---

## 🎯 2. Problemas Planteados y Algoritmos Vistos en Clase

El trabajo aborda con rigor matemático y computacional los dos problemas formulados:

### 🔹 Problema 1: Optimización de Espacio y Peso (Dimensiones y Cargas)
* **Datos evaluados:** Alto ($m$), Ancho ($m$), Profundidad ($m$), Volumen ($m^3$) y Peso ($kg$) de cada paquete.
* **Método aplicado:** **Algoritmo de la Mochila 0/1 (Knapsack 0/1)** mediante **Programación Dinámica (Bottom-Up con Tabulación)**, tal como se explicó en la **Sesión 10**.
  * Recurrencia implementada:
    $$\text{si } peso[i] > w: \quad dp[i][w] = dp[i-1][w]$$
    $$\text{si no:} \quad dp[i][w] = \max(dp[i-1][w], \, valor[i] + dp[i-1][w - peso[i]])$$
  * Permite asignar el conjunto óptimo de paquetes a cada medio de transporte (Barco, Avión, Furgón, Van, Moto), respetando los límites estrictos de peso máximo y capacidad volumétrica.
  * También se incluye la heurística Greedy (Algoritmo Ávido de la Sesión 8) por densidad de valor para contraste teórico.

### 🔹 Problema 2: Enrutamiento Óptimo y Tiempos de Entrega (Rutas y Coordenadas)
* **Datos evaluados:** Coordenadas geográficas (Latitud y Longitud) de origen y destino final de cada paquete.
* **Método aplicado:** **Algoritmo de Dijkstra** utilizando una **Cola de Prioridad Min-Heap (`heapq`)**, visto en las **Sesiones 7 y 8**.
  * Complejidad: $\mathcal{O}((V + E) \log V)$.
  * Calcula la ruta mínima intermodal garantizada pasando por puertos, aeropuertos, hubs terrestres y destino en Ibagué.
  * Calcula la distancia total en kilómetros ($km$) y el tiempo estimado de viaje en horas ($h$).

### 🔹 Estructura Adicional: Bodega Local con Árbol Binario de Búsqueda (BST)
* Implementado en `algoritmos/arbol_bodega.py` (visto en la **Sesión 6**) para ordenar y clasificar las cargas por su ID antes del despacho, permitiendo búsquedas en tiempo $\mathcal{O}(\log n)$ y recorrido inorden ascendente.

---

## 📁 3. Estructura del Código

```text
segundo semestre/
├── algoritmos/
│   ├── __init__.py
│   ├── arbol_bodega.py      # Árbol BST para organización en bodega
│   ├── dijkstra.py          # Algoritmo de Dijkstra con Min-Heap
│   └── mochila.py           # Algoritmo de la Mochila 0/1 (DP y Greedy)
├── modelos/
│   ├── __init__.py
│   ├── paquete.py           # Clase Paquete (dimensiones, volumen, peso, lat, lon)
│   └── transporte.py        # Clases de Transporte (Barco, Avión, Furgón, Van, Moto)
├── red_logistica/
│   ├── __init__.py
│   └── grafo_rutas.py       # Grafo multimodal con coordenadas y puertos
├── exportador/
│   ├── __init__.py
│   └── exportar_excel.py    # Generador de Excel profesional con openpyxl
├── visualizacion/
│   ├── simulador_mapa.html  # Simulador interactivo en Leaflet (Exoneración)
│   └── datos_simulador.js   # Datos sincronizados para el mapa
├── data/
│   └── paquetes_ejemplo.json# Cargas de prueba realistas
├── main.py                  # Menú principal interactivo de consola
├── reporte_logistica_barcos.xlsx # Archivo Excel generado automáticamente
├── .gitignore
└── README.md
```

---

## 🚀 4. Instrucciones de Ejecución en Visual Studio Code

### Requisitos Previos
* Python 3.10 o superior instalado.
* Librerías requeridas: `openpyxl` (ya instalada en el entorno).

### Paso 1: Abrir la carpeta en Visual Studio Code
Abre la carpeta `segundo semestre` en VS Code:
```bash
code .
```

### Paso 2: Ejecutar el menú principal en la terminal
```bash
python main.py
```

En pantalla aparecerá el siguiente menú interactivo:
```text
======================================================================
🚢 SISTEMA LOGÍSTICO MULTIMODAL (DIJKSTRA + MOCHILA + PUERTOS)
   Universidad - Diseño de Algoritmos (6to Semestre)
======================================================================
1. Ver Inventario de Cargas y Dimensiones (Organizado en Bodega BST)
2. Optimizar Cargas de Transporte con Algoritmo de La Mochila (Knapsack)
3. Calcular Rutas Óptimas de Entrega con Algoritmo de Dijkstra
4. Generar y Exportar Reporte Completo a Excel (.xlsx)
5. Abrir Simulador Web Interactivo de Puertos (Exoneración)
6. Ejecutar Flujo Completo Automáticamente
0. Salir
======================================================================
```

* Para ejecutar todo de una sola vez, pulsa la opción **`6`**.

---

## 📊 5. Archivo de Excel Generado (`reporte_logistica_barcos.xlsx`)

El sistema crea automáticamente un libro Excel estructurado con formato profesional:
1. **Hoja 'Resumen Ejecutivo':** Tarjetas de KPI (Total paquetes, peso total, volumen total, aprovechamiento de capacidad).
2. **Hoja '1. Inventario Paquetes':** Lista completa de cargas con sus dimensiones (Alto, Ancho, Profundidad), Volumen en $m^3$, Peso en $kg$, Destino final y coordenadas (Latitud, Longitud).
3. **Hoja '2. Optimización Mochila':** Distribución por vehículo (Barco, Avión, Furgón, Van, Moto), capacidad usada vs máxima y porcentaje de eficiencia.
4. **Hoja '3. Rutas Óptimas Dijkstra':** Desglose de cada ruta calculada, número de escalas, kilómetros totales y horas de tránsito estimadas.

---

## 🗺️ 6. Simulador Web Interactivo de Puertos (Criterio de Exoneración)

Para cumplir con el requerimiento de **exoneración** establecido en las notas de clase (*"el mapa tiene que simular bien los puertos"* y *"debe tener varios puertos"*):
* El archivo `visualizacion/simulador_mapa.html` despliega un mapa interactivo mundial con tecnología **Leaflet**:
  * **Puertos Marítimos Modelados:** Shanghái, Rotterdam, Los Ángeles, Miami, Buenaventura, Cartagena, Barranquilla y Santa Marta con sus coordenadas reales.
  * **Rutas Náuticas Animadas:** Simulación gráfica de barcos navegando por las rutas marítimas internacionales hasta los puertos colombianos.
  * **Conexión Intermodal:** Trazado de rutas desde los puertos hacia Cali, Medellín, Bogotá e Ibagué.
  * **Última Milla en Ibagué:** Distribución a comunas (Centro, El Salado, Picaleña, Mirolindo, Ricaurte).
  * **Panel de Control:** Permite seleccionar cualquier paquete y ver el camino óptimo de Dijkstra dibujado en tiempo real.

Para abrirlo:
* Desde el menú de `main.py`, elige la opción **`5`**.
* O abre directamente el archivo `visualizacion/simulador_mapa.html` en tu navegador o con la extensión Live Server de VS Code.

---

## 🎤 7. Guía Rápida para Sustentar el Parcial ante el Profesor

Cuando el docente te pregunte por el código durante la presentación:
1. **Sobre la Mochila (`algoritmos/mochila.py`):**
   * Explica que utilizaste la **matriz DP Bottom-Up con tabulación** de la Sesión 10 para garantizar el óptimo global, y que hiciste backtracking para saber con certeza qué paquetes van en el barco y cuáles en los furgones/motos.
2. **Sobre Dijkstra (`algoritmos/dijkstra.py`):**
   * Menciona que usaste una cola de prioridad basada en `heapq` (Min-Heap) para lograr una complejidad $\mathcal{O}((V + E) \log V)$ y que el grafo es multimodal porque conecta aristas de barco (40 km/h), avión (850 km/h) y terrestres (40-50 km/h).
3. **Sobre el Simulador (`simulador_mapa.html`):**
   * Muestra la simulación animada de los puertos internacionales y de Colombia (Buenaventura y Cartagena) y cómo el algoritmo recalcula la ruta y dibuja la navegación en vivo hasta Ibagué.
