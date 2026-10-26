// Archivo generado automáticamente por main.py
const COORDENADAS_NODOS = {
  "Puerto de Shanghái (China)": {
    "lat": 31.2304,
    "lon": 121.4737,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Rotterdam (Países Bajos)": {
    "lat": 51.9244,
    "lon": 4.4777,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Los Ángeles (EE.UU.)": {
    "lat": 33.7432,
    "lon": -118.2673,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Miami (EE.UU.)": {
    "lat": 25.7617,
    "lon": -80.1918,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Buenaventura (Col - Pacífico)": {
    "lat": 3.8833,
    "lon": -77.0333,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Cartagena (Col - Caribe)": {
    "lat": 10.391,
    "lon": -75.4794,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Barranquilla (Col - Caribe)": {
    "lat": 10.9685,
    "lon": -74.7813,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Puerto de Santa Marta (Col - Caribe)": {
    "lat": 11.2408,
    "lon": -74.199,
    "tipo": "puerto",
    "icono": "⚓"
  },
  "Aeropuerto Shanghái Pudong (PVG)": {
    "lat": 31.1443,
    "lon": 121.8083,
    "tipo": "aeropuerto",
    "icono": "✈️"
  },
  "Aeropuerto Ámsterdam Schiphol (AMS)": {
    "lat": 52.3105,
    "lon": 4.7683,
    "tipo": "aeropuerto",
    "icono": "✈️"
  },
  "Aeropuerto Miami Internacional (MIA)": {
    "lat": 25.7959,
    "lon": -80.287,
    "tipo": "aeropuerto",
    "icono": "✈️"
  },
  "Aeropuerto Bogotá El Dorado (BOG)": {
    "lat": 4.7016,
    "lon": -74.1469,
    "tipo": "aeropuerto",
    "icono": "✈️"
  },
  "Cali (Hub Pacífico)": {
    "lat": 3.4516,
    "lon": -76.532,
    "tipo": "hub_terrestre",
    "icono": "🏢"
  },
  "Medellín (Hub Central)": {
    "lat": 6.2442,
    "lon": -75.5812,
    "tipo": "hub_terrestre",
    "icono": "🏢"
  },
  "Bucaramanga (Hub Oriente)": {
    "lat": 7.1254,
    "lon": -73.1198,
    "tipo": "hub_terrestre",
    "icono": "🏢"
  },
  "Ibagué (Hub Central Tolima)": {
    "lat": 4.4389,
    "lon": -75.2322,
    "tipo": "hub_principal",
    "icono": "🏬"
  },
  "Ibagué - Zona Centro (Comuna 1)": {
    "lat": 4.4446,
    "lon": -75.241,
    "tipo": "destino_urbano",
    "icono": "🛵"
  },
  "Ibagué - El Salado (Comuna 7)": {
    "lat": 4.4764,
    "lon": -75.1856,
    "tipo": "destino_urbano",
    "icono": "🚐"
  },
  "Ibagué - Picaleña / Parque Ind. (Comuna 9)": {
    "lat": 4.4082,
    "lon": -75.1583,
    "tipo": "destino_urbano",
    "icono": "🚛"
  },
  "Ibagué - Mirolindo (Comuna 9)": {
    "lat": 4.4251,
    "lon": -75.1989,
    "tipo": "destino_urbano",
    "icono": "🚐"
  },
  "Ibagué - Ricaurte (Comuna 12)": {
    "lat": 4.4211,
    "lon": -75.2415,
    "tipo": "destino_urbano",
    "icono": "🛵"
  }
};

const PAQUETES_DATA = [
  {
    "id_paquete": 101,
    "descripcion": "Maquinaria Textil Industrial (Contenedor)",
    "alto_m": 2.6,
    "ancho_m": 2.4,
    "profundidad_m": 6.0,
    "volumen_m3": 37.44,
    "peso_kg": 8500.0,
    "origen": "Puerto de Shanghái (China)",
    "destino_nombre": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
    "lat": 4.4082,
    "lon": -75.1583,
    "modalidad_preferida": "barco",
    "prioridad": 85
  },
  {
    "id_paquete": 102,
    "descripcion": "Lote Repuestos Automotrices Pesados",
    "alto_m": 1.8,
    "ancho_m": 1.5,
    "profundidad_m": 2.2,
    "volumen_m3": 5.94,
    "peso_kg": 3200.0,
    "origen": "Puerto de Rotterdam (Países Bajos)",
    "destino_nombre": "Ibagué - Mirolindo (Comuna 9)",
    "lat": 4.4251,
    "lon": -75.1989,
    "modalidad_preferida": "barco",
    "prioridad": 75
  },
  {
    "id_paquete": 103,
    "descripcion": "Bobinas de Acero y Perfilería",
    "alto_m": 1.5,
    "ancho_m": 1.5,
    "profundidad_m": 3.0,
    "volumen_m3": 6.75,
    "peso_kg": 5400.0,
    "origen": "Puerto de Shanghái (China)",
    "destino_nombre": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
    "lat": 4.4082,
    "lon": -75.1583,
    "modalidad_preferida": "barco",
    "prioridad": 70
  },
  {
    "id_paquete": 104,
    "descripcion": "Equipos Médicos de Alta Precisión (Urgente)",
    "alto_m": 1.2,
    "ancho_m": 0.9,
    "profundidad_m": 1.1,
    "volumen_m3": 1.188,
    "peso_kg": 180.0,
    "origen": "Aeropuerto Miami Internacional (MIA)",
    "destino_nombre": "Ibagué - Zona Centro (Comuna 1)",
    "lat": 4.4446,
    "lon": -75.241,
    "modalidad_preferida": "avion",
    "prioridad": 98
  },
  {
    "id_paquete": 105,
    "descripcion": "Servidores y Racks de Telecomunicaciones",
    "alto_m": 2.0,
    "ancho_m": 0.8,
    "profundidad_m": 1.0,
    "volumen_m3": 1.6,
    "peso_kg": 420.0,
    "origen": "Aeropuerto Shanghái Pudong (PVG)",
    "destino_nombre": "Ibagué - Mirolindo (Comuna 9)",
    "lat": 4.4251,
    "lon": -75.1989,
    "modalidad_preferida": "avion",
    "prioridad": 92
  },
  {
    "id_paquete": 106,
    "descripcion": "Insumos Químicos y Fertilizantes Agrícolas",
    "alto_m": 1.4,
    "ancho_m": 1.2,
    "profundidad_m": 1.8,
    "volumen_m3": 3.024,
    "peso_kg": 2100.0,
    "origen": "Puerto de Miami (EE.UU.)",
    "destino_nombre": "Ibagué - El Salado (Comuna 7)",
    "lat": 4.4764,
    "lon": -75.1856,
    "modalidad_preferida": "barco",
    "prioridad": 65
  },
  {
    "id_paquete": 107,
    "descripcion": "Electrodomésticos y Neveras Comerciales",
    "alto_m": 1.9,
    "ancho_m": 1.1,
    "profundidad_m": 1.2,
    "volumen_m3": 2.508,
    "peso_kg": 850.0,
    "origen": "Puerto de Shanghái (China)",
    "destino_nombre": "Ibagué - Mirolindo (Comuna 9)",
    "lat": 4.4251,
    "lon": -75.1989,
    "modalidad_preferida": "barco",
    "prioridad": 60
  },
  {
    "id_paquete": 108,
    "descripcion": "Cajas de Calzado y Textiles para Comercio",
    "alto_m": 0.8,
    "ancho_m": 0.6,
    "profundidad_m": 0.9,
    "volumen_m3": 0.432,
    "peso_kg": 95.0,
    "origen": "Puerto de Miami (EE.UU.)",
    "destino_nombre": "Ibagué - Zona Centro (Comuna 1)",
    "lat": 4.4446,
    "lon": -75.241,
    "modalidad_preferida": "barco",
    "prioridad": 55
  },
  {
    "id_paquete": 109,
    "descripcion": "Medicamentos Refrigerados y Vacunas",
    "alto_m": 0.6,
    "ancho_m": 0.5,
    "profundidad_m": 0.5,
    "volumen_m3": 0.15,
    "peso_kg": 28.0,
    "origen": "Aeropuerto Ámsterdam Schiphol (AMS)",
    "destino_nombre": "Ibagué - Zona Centro (Comuna 1)",
    "lat": 4.4446,
    "lon": -75.241,
    "modalidad_preferida": "avion",
    "prioridad": 99
  },
  {
    "id_paquete": 110,
    "descripcion": "Documentación Notarial y Contratos Urgentes",
    "alto_m": 0.1,
    "ancho_m": 0.25,
    "profundidad_m": 0.35,
    "volumen_m3": 0.009,
    "peso_kg": 3.5,
    "origen": "Aeropuerto Bogotá El Dorado (BOG)",
    "destino_nombre": "Ibagué - Ricaurte (Comuna 12)",
    "lat": 4.4211,
    "lon": -75.2415,
    "modalidad_preferida": "avion",
    "prioridad": 90
  },
  {
    "id_paquete": 111,
    "descripcion": "Paquete Repuestos de Drones y Microelectrónica",
    "alto_m": 0.3,
    "ancho_m": 0.3,
    "profundidad_m": 0.4,
    "volumen_m3": 0.036,
    "peso_kg": 8.0,
    "origen": "Aeropuerto Shanghái Pudong (PVG)",
    "destino_nombre": "Ibagué - Zona Centro (Comuna 1)",
    "lat": 4.4446,
    "lon": -75.241,
    "modalidad_preferida": "avion",
    "prioridad": 88
  },
  {
    "id_paquete": 112,
    "descripcion": "Caja Herramientas Eléctricas para Taller",
    "alto_m": 0.5,
    "ancho_m": 0.4,
    "profundidad_m": 0.6,
    "volumen_m3": 0.12,
    "peso_kg": 45.0,
    "origen": "Puerto de Rotterdam (Países Bajos)",
    "destino_nombre": "Ibagué - El Salado (Comuna 7)",
    "lat": 4.4764,
    "lon": -75.1856,
    "modalidad_preferida": "barco",
    "prioridad": 50
  }
];

const RUTAS_DIJKSTRA_DATA = [
  {
    "id_paquete": 101,
    "descripcion": "Maquinaria Textil Industrial (Contenedor)",
    "origen": "Puerto de Shanghái (China)",
    "destino": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
    "ruta": [
      "Puerto de Shanghái (China)",
      "Puerto de Buenaventura (Col - Pacífico)",
      "Cali (Hub Pacífico)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Picaleña / Parque Ind. (Comuna 9)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Shanghái (China)",
        "hasta": "Puerto de Buenaventura (Col - Pacífico)",
        "modo": "barco",
        "distancia_km": 15400,
        "tiempo_h": 385.0
      },
      {
        "desde": "Puerto de Buenaventura (Col - Pacífico)",
        "hasta": "Cali (Hub Pacífico)",
        "modo": "terrestre",
        "distancia_km": 125,
        "tiempo_h": 3.0
      },
      {
        "desde": "Cali (Hub Pacífico)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 242,
        "tiempo_h": 5.5
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
        "modo": "furgon",
        "distancia_km": 9.8,
        "tiempo_h": 0.35
      }
    ],
    "distancia_km": 15776.8,
    "tiempo_h": 393.85
  },
  {
    "id_paquete": 102,
    "descripcion": "Lote Repuestos Automotrices Pesados",
    "origen": "Puerto de Rotterdam (Países Bajos)",
    "destino": "Ibagué - Mirolindo (Comuna 9)",
    "ruta": [
      "Puerto de Rotterdam (Países Bajos)",
      "Puerto de Cartagena (Col - Caribe)",
      "Medellín (Hub Central)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Mirolindo (Comuna 9)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Rotterdam (Países Bajos)",
        "hasta": "Puerto de Cartagena (Col - Caribe)",
        "modo": "barco",
        "distancia_km": 8400,
        "tiempo_h": 210.0
      },
      {
        "desde": "Puerto de Cartagena (Col - Caribe)",
        "hasta": "Medellín (Hub Central)",
        "modo": "terrestre",
        "distancia_km": 635,
        "tiempo_h": 11.5
      },
      {
        "desde": "Medellín (Hub Central)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 395,
        "tiempo_h": 7.8
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Mirolindo (Comuna 9)",
        "modo": "van",
        "distancia_km": 6.2,
        "tiempo_h": 0.3
      }
    ],
    "distancia_km": 9436.2,
    "tiempo_h": 229.6
  },
  {
    "id_paquete": 103,
    "descripcion": "Bobinas de Acero y Perfilería",
    "origen": "Puerto de Shanghái (China)",
    "destino": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
    "ruta": [
      "Puerto de Shanghái (China)",
      "Puerto de Buenaventura (Col - Pacífico)",
      "Cali (Hub Pacífico)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Picaleña / Parque Ind. (Comuna 9)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Shanghái (China)",
        "hasta": "Puerto de Buenaventura (Col - Pacífico)",
        "modo": "barco",
        "distancia_km": 15400,
        "tiempo_h": 385.0
      },
      {
        "desde": "Puerto de Buenaventura (Col - Pacífico)",
        "hasta": "Cali (Hub Pacífico)",
        "modo": "terrestre",
        "distancia_km": 125,
        "tiempo_h": 3.0
      },
      {
        "desde": "Cali (Hub Pacífico)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 242,
        "tiempo_h": 5.5
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Picaleña / Parque Ind. (Comuna 9)",
        "modo": "furgon",
        "distancia_km": 9.8,
        "tiempo_h": 0.35
      }
    ],
    "distancia_km": 15776.8,
    "tiempo_h": 393.85
  },
  {
    "id_paquete": 104,
    "descripcion": "Equipos Médicos de Alta Precisión (Urgente)",
    "origen": "Aeropuerto Miami Internacional (MIA)",
    "destino": "Ibagué - Zona Centro (Comuna 1)",
    "ruta": [
      "Aeropuerto Miami Internacional (MIA)",
      "Aeropuerto Bogotá El Dorado (BOG)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Zona Centro (Comuna 1)"
    ],
    "tramos": [
      {
        "desde": "Aeropuerto Miami Internacional (MIA)",
        "hasta": "Aeropuerto Bogotá El Dorado (BOG)",
        "modo": "avion",
        "distancia_km": 2430,
        "tiempo_h": 3.8
      },
      {
        "desde": "Aeropuerto Bogotá El Dorado (BOG)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 200,
        "tiempo_h": 4.2
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Zona Centro (Comuna 1)",
        "modo": "moto",
        "distancia_km": 4.5,
        "tiempo_h": 0.25
      }
    ],
    "distancia_km": 2634.5,
    "tiempo_h": 8.25
  },
  {
    "id_paquete": 105,
    "descripcion": "Servidores y Racks de Telecomunicaciones",
    "origen": "Aeropuerto Shanghái Pudong (PVG)",
    "destino": "Ibagué - Mirolindo (Comuna 9)",
    "ruta": [
      "Aeropuerto Shanghái Pudong (PVG)",
      "Aeropuerto Bogotá El Dorado (BOG)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Mirolindo (Comuna 9)"
    ],
    "tramos": [
      {
        "desde": "Aeropuerto Shanghái Pudong (PVG)",
        "hasta": "Aeropuerto Bogotá El Dorado (BOG)",
        "modo": "avion",
        "distancia_km": 15800,
        "tiempo_h": 19.5
      },
      {
        "desde": "Aeropuerto Bogotá El Dorado (BOG)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 200,
        "tiempo_h": 4.2
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Mirolindo (Comuna 9)",
        "modo": "van",
        "distancia_km": 6.2,
        "tiempo_h": 0.3
      }
    ],
    "distancia_km": 16006.2,
    "tiempo_h": 24.0
  },
  {
    "id_paquete": 106,
    "descripcion": "Insumos Químicos y Fertilizantes Agrícolas",
    "origen": "Puerto de Miami (EE.UU.)",
    "destino": "Ibagué - El Salado (Comuna 7)",
    "ruta": [
      "Puerto de Miami (EE.UU.)",
      "Puerto de Cartagena (Col - Caribe)",
      "Medellín (Hub Central)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - El Salado (Comuna 7)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Miami (EE.UU.)",
        "hasta": "Puerto de Cartagena (Col - Caribe)",
        "modo": "barco",
        "distancia_km": 1800,
        "tiempo_h": 45.0
      },
      {
        "desde": "Puerto de Cartagena (Col - Caribe)",
        "hasta": "Medellín (Hub Central)",
        "modo": "terrestre",
        "distancia_km": 635,
        "tiempo_h": 11.5
      },
      {
        "desde": "Medellín (Hub Central)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 395,
        "tiempo_h": 7.8
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - El Salado (Comuna 7)",
        "modo": "van",
        "distancia_km": 11.2,
        "tiempo_h": 0.45
      }
    ],
    "distancia_km": 2841.2,
    "tiempo_h": 64.75
  },
  {
    "id_paquete": 107,
    "descripcion": "Electrodomésticos y Neveras Comerciales",
    "origen": "Puerto de Shanghái (China)",
    "destino": "Ibagué - Mirolindo (Comuna 9)",
    "ruta": [
      "Puerto de Shanghái (China)",
      "Puerto de Buenaventura (Col - Pacífico)",
      "Cali (Hub Pacífico)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Mirolindo (Comuna 9)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Shanghái (China)",
        "hasta": "Puerto de Buenaventura (Col - Pacífico)",
        "modo": "barco",
        "distancia_km": 15400,
        "tiempo_h": 385.0
      },
      {
        "desde": "Puerto de Buenaventura (Col - Pacífico)",
        "hasta": "Cali (Hub Pacífico)",
        "modo": "terrestre",
        "distancia_km": 125,
        "tiempo_h": 3.0
      },
      {
        "desde": "Cali (Hub Pacífico)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 242,
        "tiempo_h": 5.5
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Mirolindo (Comuna 9)",
        "modo": "van",
        "distancia_km": 6.2,
        "tiempo_h": 0.3
      }
    ],
    "distancia_km": 15773.2,
    "tiempo_h": 393.8
  },
  {
    "id_paquete": 108,
    "descripcion": "Cajas de Calzado y Textiles para Comercio",
    "origen": "Puerto de Miami (EE.UU.)",
    "destino": "Ibagué - Zona Centro (Comuna 1)",
    "ruta": [
      "Puerto de Miami (EE.UU.)",
      "Puerto de Cartagena (Col - Caribe)",
      "Medellín (Hub Central)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Zona Centro (Comuna 1)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Miami (EE.UU.)",
        "hasta": "Puerto de Cartagena (Col - Caribe)",
        "modo": "barco",
        "distancia_km": 1800,
        "tiempo_h": 45.0
      },
      {
        "desde": "Puerto de Cartagena (Col - Caribe)",
        "hasta": "Medellín (Hub Central)",
        "modo": "terrestre",
        "distancia_km": 635,
        "tiempo_h": 11.5
      },
      {
        "desde": "Medellín (Hub Central)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 395,
        "tiempo_h": 7.8
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Zona Centro (Comuna 1)",
        "modo": "moto",
        "distancia_km": 4.5,
        "tiempo_h": 0.25
      }
    ],
    "distancia_km": 2834.5,
    "tiempo_h": 64.55
  },
  {
    "id_paquete": 109,
    "descripcion": "Medicamentos Refrigerados y Vacunas",
    "origen": "Aeropuerto Ámsterdam Schiphol (AMS)",
    "destino": "Ibagué - Zona Centro (Comuna 1)",
    "ruta": [
      "Aeropuerto Ámsterdam Schiphol (AMS)",
      "Aeropuerto Bogotá El Dorado (BOG)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Zona Centro (Comuna 1)"
    ],
    "tramos": [
      {
        "desde": "Aeropuerto Ámsterdam Schiphol (AMS)",
        "hasta": "Aeropuerto Bogotá El Dorado (BOG)",
        "modo": "avion",
        "distancia_km": 8850,
        "tiempo_h": 11.2
      },
      {
        "desde": "Aeropuerto Bogotá El Dorado (BOG)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 200,
        "tiempo_h": 4.2
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Zona Centro (Comuna 1)",
        "modo": "moto",
        "distancia_km": 4.5,
        "tiempo_h": 0.25
      }
    ],
    "distancia_km": 9054.5,
    "tiempo_h": 15.65
  },
  {
    "id_paquete": 110,
    "descripcion": "Documentación Notarial y Contratos Urgentes",
    "origen": "Aeropuerto Bogotá El Dorado (BOG)",
    "destino": "Ibagué - Ricaurte (Comuna 12)",
    "ruta": [
      "Aeropuerto Bogotá El Dorado (BOG)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Ricaurte (Comuna 12)"
    ],
    "tramos": [
      {
        "desde": "Aeropuerto Bogotá El Dorado (BOG)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 200,
        "tiempo_h": 4.2
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Ricaurte (Comuna 12)",
        "modo": "moto",
        "distancia_km": 5.1,
        "tiempo_h": 0.28
      }
    ],
    "distancia_km": 205.1,
    "tiempo_h": 4.48
  },
  {
    "id_paquete": 111,
    "descripcion": "Paquete Repuestos de Drones y Microelectrónica",
    "origen": "Aeropuerto Shanghái Pudong (PVG)",
    "destino": "Ibagué - Zona Centro (Comuna 1)",
    "ruta": [
      "Aeropuerto Shanghái Pudong (PVG)",
      "Aeropuerto Bogotá El Dorado (BOG)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - Zona Centro (Comuna 1)"
    ],
    "tramos": [
      {
        "desde": "Aeropuerto Shanghái Pudong (PVG)",
        "hasta": "Aeropuerto Bogotá El Dorado (BOG)",
        "modo": "avion",
        "distancia_km": 15800,
        "tiempo_h": 19.5
      },
      {
        "desde": "Aeropuerto Bogotá El Dorado (BOG)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 200,
        "tiempo_h": 4.2
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - Zona Centro (Comuna 1)",
        "modo": "moto",
        "distancia_km": 4.5,
        "tiempo_h": 0.25
      }
    ],
    "distancia_km": 16004.5,
    "tiempo_h": 23.95
  },
  {
    "id_paquete": 112,
    "descripcion": "Caja Herramientas Eléctricas para Taller",
    "origen": "Puerto de Rotterdam (Países Bajos)",
    "destino": "Ibagué - El Salado (Comuna 7)",
    "ruta": [
      "Puerto de Rotterdam (Países Bajos)",
      "Puerto de Cartagena (Col - Caribe)",
      "Medellín (Hub Central)",
      "Ibagué (Hub Central Tolima)",
      "Ibagué - El Salado (Comuna 7)"
    ],
    "tramos": [
      {
        "desde": "Puerto de Rotterdam (Países Bajos)",
        "hasta": "Puerto de Cartagena (Col - Caribe)",
        "modo": "barco",
        "distancia_km": 8400,
        "tiempo_h": 210.0
      },
      {
        "desde": "Puerto de Cartagena (Col - Caribe)",
        "hasta": "Medellín (Hub Central)",
        "modo": "terrestre",
        "distancia_km": 635,
        "tiempo_h": 11.5
      },
      {
        "desde": "Medellín (Hub Central)",
        "hasta": "Ibagué (Hub Central Tolima)",
        "modo": "terrestre",
        "distancia_km": 395,
        "tiempo_h": 7.8
      },
      {
        "desde": "Ibagué (Hub Central Tolima)",
        "hasta": "Ibagué - El Salado (Comuna 7)",
        "modo": "van",
        "distancia_km": 11.2,
        "tiempo_h": 0.45
      }
    ],
    "distancia_km": 9441.2,
    "tiempo_h": 229.75
  }
];
