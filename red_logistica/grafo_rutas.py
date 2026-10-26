# Red de transporte con puertos, aeropuertos y rutas a Ibague
# Aviones (pais a pais), Barcos (puerto a puerto) y Terrestre (Ibague)


# Coordenadas geográficas exactas (Latitud, Longitud) de cada nodo
COORDENADAS_NODOS = {
    # --- PUERTOS MARÍTIMOS (Barcos: Puerto a Puerto) ---
    "Puerto de Shanghái (China)": {"lat": 31.2304, "lon": 121.4737, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Rotterdam (Países Bajos)": {"lat": 51.9244, "lon": 4.4777, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Los Ángeles (EE.UU.)": {"lat": 33.7432, "lon": -118.2673, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Miami (EE.UU.)": {"lat": 25.7617, "lon": -80.1918, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Buenaventura (Col - Pacífico)": {"lat": 3.8833, "lon": -77.0333, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Cartagena (Col - Caribe)": {"lat": 10.3910, "lon": -75.4794, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Barranquilla (Col - Caribe)": {"lat": 10.9685, "lon": -74.7813, "tipo": "puerto", "icono": "⚓"},
    "Puerto de Santa Marta (Col - Caribe)": {"lat": 11.2408, "lon": -74.1990, "tipo": "puerto", "icono": "⚓"},

    # --- AEROPUERTOS INTERNACIONALES (Aviones: País a País) ---
    "Aeropuerto Shanghái Pudong (PVG)": {"lat": 31.1443, "lon": 121.8083, "tipo": "aeropuerto", "icono": "✈️"},
    "Aeropuerto Ámsterdam Schiphol (AMS)": {"lat": 52.3105, "lon": 4.7683, "tipo": "aeropuerto", "icono": "✈️"},
    "Aeropuerto Miami Internacional (MIA)": {"lat": 25.7959, "lon": -80.2870, "tipo": "aeropuerto", "icono": "✈️"},
    "Aeropuerto Bogotá El Dorado (BOG)": {"lat": 4.7016, "lon": -74.1469, "tipo": "aeropuerto", "icono": "✈️"},

    # --- HUBS TERRESTRES NACIONALES ---
    "Cali (Hub Pacífico)": {"lat": 3.4516, "lon": -76.5320, "tipo": "hub_terrestre", "icono": "🏢"},
    "Medellín (Hub Central)": {"lat": 6.2442, "lon": -75.5812, "tipo": "hub_terrestre", "icono": "🏢"},
    "Bucaramanga (Hub Oriente)": {"lat": 7.1254, "lon": -73.1198, "tipo": "hub_terrestre", "icono": "🏢"},

    # --- CENTRO LOGÍSTICO Y ZONAS URBANAS EN IBAGUÉ (TOLIMA) ---
    "Ibagué (Hub Central Tolima)": {"lat": 4.4389, "lon": -75.2322, "tipo": "hub_principal", "icono": "🏬"},
    "Ibagué - Zona Centro (Comuna 1)": {"lat": 4.4446, "lon": -75.2410, "tipo": "destino_urbano", "icono": "🛵"},
    "Ibagué - El Salado (Comuna 7)": {"lat": 4.4764, "lon": -75.1856, "tipo": "destino_urbano", "icono": "🚐"},
    "Ibagué - Picaleña / Parque Ind. (Comuna 9)": {"lat": 4.4082, "lon": -75.1583, "tipo": "destino_urbano", "icono": "🚛"},
    "Ibagué - Mirolindo (Comuna 9)": {"lat": 4.4251, "lon": -75.1989, "tipo": "destino_urbano", "icono": "🚐"},
    "Ibagué - Ricaurte (Comuna 12)": {"lat": 4.4211, "lon": -75.2415, "tipo": "destino_urbano", "icono": "🛵"}
}


class RedMultimodalLogistica:
    """
    Grafo que unifica la red mundial de puertos (marítimo),
    red aérea de aeropuertos, conexiones nacionales y la red urbana de Ibagué.
    """
    def __init__(self):
        # Lista de adyacencia: nodo -> [(vecino, distancia_km, modo_transporte, tiempo_horas)]
        self.grafo = {}
        self._construir_red()

    def agregar_conexion(self, origen, destino, distancia_km, modo, tiempo_horas, bidireccional=True):
        if origen not in self.grafo:
            self.grafo[origen] = []
        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origen].append((destino, distancia_km, modo, tiempo_horas))
        if bidireccional:
            self.grafo[destino].append((origen, distancia_km, modo, tiempo_horas))

    def _construir_red(self):
        # -------------------------------------------------------------
        # 1. RUTAS MARÍTIMAS: BARCOS (Puerto a Puerto) - Varios Puertos
        # -------------------------------------------------------------
        # Shanghái -> Buenaventura (Océano Pacífico directo)
        self.agregar_conexion(
            "Puerto de Shanghái (China)", 
            "Puerto de Buenaventura (Col - Pacífico)", 
            15400, "barco", 385.0
        )
        # Shanghái -> Los Ángeles -> Buenaventura
        self.agregar_conexion(
            "Puerto de Shanghái (China)", 
            "Puerto de Los Ángeles (EE.UU.)", 
            10500, "barco", 262.5
        )
        self.agregar_conexion(
            "Puerto de Los Ángeles (EE.UU.)", 
            "Puerto de Buenaventura (Col - Pacífico)", 
            5500, "barco", 137.5
        )
        # Rotterdam -> Miami -> Cartagena
        self.agregar_conexion(
            "Puerto de Rotterdam (Países Bajos)", 
            "Puerto de Miami (EE.UU.)", 
            7600, "barco", 190.0
        )
        self.agregar_conexion(
            "Puerto de Rotterdam (Países Bajos)", 
            "Puerto de Cartagena (Col - Caribe)", 
            8400, "barco", 210.0
        )
        self.agregar_conexion(
            "Puerto de Miami (EE.UU.)", 
            "Puerto de Cartagena (Col - Caribe)", 
            1800, "barco", 45.0
        )
        self.agregar_conexion(
            "Puerto de Miami (EE.UU.)", 
            "Puerto de Barranquilla (Col - Caribe)", 
            1850, "barco", 46.2
        )
        # Rutas de cabotaje Caribe colombiano
        self.agregar_conexion(
            "Puerto de Cartagena (Col - Caribe)", 
            "Puerto de Barranquilla (Col - Caribe)", 
            120, "barco", 3.0
        )
        self.agregar_conexion(
            "Puerto de Barranquilla (Col - Caribe)", 
            "Puerto de Santa Marta (Col - Caribe)", 
            85, "barco", 2.1
        )

        # -------------------------------------------------------------
        # 2. RUTAS AÉREAS: AVIONES (País a País)
        # -------------------------------------------------------------
        self.agregar_conexion(
            "Aeropuerto Shanghái Pudong (PVG)", 
            "Aeropuerto Bogotá El Dorado (BOG)", 
            15800, "avion", 19.5
        )
        self.agregar_conexion(
            "Aeropuerto Ámsterdam Schiphol (AMS)", 
            "Aeropuerto Bogotá El Dorado (BOG)", 
            8850, "avion", 11.2
        )
        self.agregar_conexion(
            "Aeropuerto Miami Internacional (MIA)", 
            "Aeropuerto Bogotá El Dorado (BOG)", 
            2430, "avion", 3.8
        )

        # -------------------------------------------------------------
        # 3. CONEXIÓN NACIONAL TERRESTRE HACIA IBAGUÉ
        # (Con las distancias de las clases del profesor)
        # -------------------------------------------------------------
        # Buenaventura -> Cali (125 km)
        self.agregar_conexion(
            "Puerto de Buenaventura (Col - Pacífico)", 
            "Cali (Hub Pacífico)", 
            125, "terrestre", 3.0
        )
        # Cali -> Ibagué (242 km - como en la clase de Algoritmos)
        self.agregar_conexion(
            "Cali (Hub Pacífico)", 
            "Ibagué (Hub Central Tolima)", 
            242, "terrestre", 5.5
        )
        # Bogotá El Dorado -> Ibagué (200 km - como en la clase de Algoritmos)
        self.agregar_conexion(
            "Aeropuerto Bogotá El Dorado (BOG)", 
            "Ibagué (Hub Central Tolima)", 
            200, "terrestre", 4.2
        )
        # Cartagena -> Medellín -> Ibagué
        self.agregar_conexion(
            "Puerto de Cartagena (Col - Caribe)", 
            "Medellín (Hub Central)", 
            635, "terrestre", 11.5
        )
        self.agregar_conexion(
            "Medellín (Hub Central)", 
            "Ibagué (Hub Central Tolima)", 
            395, "terrestre", 7.8
        )
        # Barranquilla / Santa Marta -> Bucaramanga -> Bogotá -> Ibagué
        self.agregar_conexion(
            "Puerto de Barranquilla (Col - Caribe)", 
            "Bucaramanga (Hub Oriente)", 
            580, "terrestre", 10.0
        )
        self.agregar_conexion(
            "Puerto de Santa Marta (Col - Caribe)", 
            "Bucaramanga (Hub Oriente)", 
            530, "terrestre", 9.2
        )
        self.agregar_conexion(
            "Bucaramanga (Hub Oriente)", 
            "Aeropuerto Bogotá El Dorado (BOG)", 
            390, "terrestre", 7.0
        )

        # -------------------------------------------------------------
        # 4. DISTRIBUCIÓN URBANA EN IBAGUÉ (FURGONES, VANS, MOTOS)
        # -------------------------------------------------------------
        # Hub Central Tolima -> Zona Centro (Motos y Vans)
        self.agregar_conexion(
            "Ibagué (Hub Central Tolima)", 
            "Ibagué - Zona Centro (Comuna 1)", 
            4.5, "moto", 0.25
        )
        # Hub Central Tolima -> El Salado (Vans)
        self.agregar_conexion(
            "Ibagué (Hub Central Tolima)", 
            "Ibagué - El Salado (Comuna 7)", 
            11.2, "van", 0.45
        )
        # Hub Central Tolima -> Picaleña / Parque Industrial (Furgones)
        self.agregar_conexion(
            "Ibagué (Hub Central Tolima)", 
            "Ibagué - Picaleña / Parque Ind. (Comuna 9)", 
            9.8, "furgon", 0.35
        )
        # Hub Central Tolima -> Mirolindo (Vans y Furgones)
        self.agregar_conexion(
            "Ibagué (Hub Central Tolima)", 
            "Ibagué - Mirolindo (Comuna 9)", 
            6.2, "van", 0.30
        )
        # Hub Central Tolima -> Ricaurte (Motos y Vans)
        self.agregar_conexion(
            "Ibagué (Hub Central Tolima)", 
            "Ibagué - Ricaurte (Comuna 12)", 
            5.1, "moto", 0.28
        )
        # Interconexiones urbanas
        self.agregar_conexion(
            "Ibagué - Mirolindo (Comuna 9)", 
            "Ibagué - Picaleña / Parque Ind. (Comuna 9)", 
            4.6, "furgon", 0.20
        )
        self.agregar_conexion(
            "Ibagué - Zona Centro (Comuna 1)", 
            "Ibagué - Ricaurte (Comuna 12)", 
            3.2, "moto", 0.18
        )
