# Red maritima de puertos y rutas para transporte en barcos
# Barcos: Carga de Puerto a Puerto (Varios puertos internacionales y colombianos)

COORDENADAS_PUERTOS = {
    "Puerto de Shanghái (China)": {"lat": 31.2304, "lon": 121.4737},
    "Puerto de Rotterdam (Países Bajos)": {"lat": 51.9244, "lon": 4.4777},
    "Puerto de Los Ángeles (EE.UU.)": {"lat": 33.7432, "lon": -118.2673},
    "Puerto de Miami (EE.UU.)": {"lat": 25.7617, "lon": -80.1918},
    "Puerto de Buenaventura (Colombia)": {"lat": 3.8833, "lon": -77.0333},
    "Puerto de Cartagena (Colombia)": {"lat": 10.3910, "lon": -75.4794},
    "Puerto de Barranquilla (Colombia)": {"lat": 10.9685, "lon": -74.7813},
    "Puerto de Santa Marta (Colombia)": {"lat": 11.2408, "lon": -74.1990}
}


class RedMaritimaPuertos:
    """Grafo de rutas maritimas entre puertos (Grafo Ponderado con Lista de Adyacencia)"""
    def __init__(self):
        self.grafo = {}
        self._construir_rutas_maritimas()

    def agregar_ruta(self, origen, destino, distancia_km, tiempo_horas, bidireccional=True):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origen].append((destino, distancia_km, "barco", tiempo_horas))
        if bidireccional:
            self.grafo[destino].append((origen, distancia_km, "barco", tiempo_horas))

    def _construir_rutas_maritimas(self):
        # Rutas del Oceano Pacifico
        # Shanghai -> Los Angeles (10,500 km)
        self.agregar_ruta("Puerto de Shanghái (China)", "Puerto de Los Ángeles (EE.UU.)", 10500, 262.5)

        # Los Angeles -> Buenaventura (5,500 km)
        self.agregar_ruta("Puerto de Los Ángeles (EE.UU.)", "Puerto de Buenaventura (Colombia)", 5500, 137.5)

        # Ruta directa transpacifica: Shanghai -> Buenaventura (15,400 km)
        self.agregar_ruta("Puerto de Shanghái (China)", "Puerto de Buenaventura (Colombia)", 15400, 385.0)

        # Rutas del Oceano Atlantico
        # Rotterdam -> Miami (7,600 km)
        self.agregar_ruta("Puerto de Rotterdam (Países Bajos)", "Puerto de Miami (EE.UU.)", 7600, 190.0)

        # Rotterdam -> Cartagena (8,400 km)
        self.agregar_ruta("Puerto de Rotterdam (Países Bajos)", "Puerto de Cartagena (Colombia)", 8400, 210.0)

        # Miami -> Cartagena (1,800 km)
        self.agregar_ruta("Puerto de Miami (EE.UU.)", "Puerto de Cartagena (Colombia)", 1800, 45.0)

        # Miami -> Barranquilla (1,850 km)
        self.agregar_ruta("Puerto de Miami (EE.UU)", "Puerto de Barranquilla (Colombia)", 1850, 46.2)

        # Rutas de cabotaje costero entre puertos colombianos
        # Cartagena <-> Barranquilla (120 km)
        self.agregar_ruta("Puerto de Cartagena (Colombia)", "Puerto de Barranquilla (Colombia)", 120, 3.0)

        # Barranquilla <-> Santa Marta (85 km)
        self.agregar_ruta("Puerto de Barranquilla (Colombia)", "Puerto de Santa Marta (Colombia)", 85, 2.1)

        # Paso por Canal de Panama conectando el Caribe con el Pacifico:
        # Cartagena <-> Buenaventura (750 km por canal interoceanico)
        self.agregar_ruta("Puerto de Cartagena (Colombia)", "Puerto de Buenaventura (Colombia)", 750, 18.5)
