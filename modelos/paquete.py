import json

class Paquete:
    """
    Representa una carga o paquete logístico según los requerimientos:
    - Dimensiones: Alto, Ancho, Profundidad (en metros)
    - Volumen calculado automáticamente: Alto * Ancho * Profundidad (m^3)
    - Peso (en kg)
    - Coordenadas de destino: Latitud y Longitud
    - Modalidad y Prioridad
    """
    def __init__(self, id_paquete, descripcion, alto, ancho, profundidad, peso_kg, 
                 origen, destino_nombre, lat, lon, modalidad_preferida="barco", prioridad=1):
        self.id_paquete = id_paquete
        self.descripcion = descripcion
        self.alto = round(float(alto), 2)
        self.ancho = round(float(ancho), 2)
        self.profundidad = round(float(profundidad), 2)
        self.volumen_m3 = round(self.alto * self.ancho * self.profundidad, 3)
        self.peso_kg = round(float(peso_kg), 2)
        self.origen = origen
        self.destino_nombre = destino_nombre
        self.lat = float(lat)
        self.lon = float(lon)
        self.modalidad_preferida = modalidad_preferida.lower()
        self.prioridad = int(prioridad)  # Valor para el algoritmo de la mochila (1 a 100)

    @property
    def densidad_peso(self):
        """Relación peso / volumen para análisis logístico"""
        return round(self.peso_kg / max(self.volumen_m3, 0.001), 2)

    def to_dict(self):
        return {
            "id_paquete": self.id_paquete,
            "descripcion": self.descripcion,
            "alto_m": self.alto,
            "ancho_m": self.ancho,
            "profundidad_m": self.profundidad,
            "volumen_m3": self.volumen_m3,
            "peso_kg": self.peso_kg,
            "origen": self.origen,
            "destino_nombre": self.destino_nombre,
            "lat": self.lat,
            "lon": self.lon,
            "modalidad_preferida": self.modalidad_preferida,
            "prioridad": self.prioridad
        }

    def __repr__(self):
        return (f"<Paquete {self.id_paquete}: {self.descripcion} | "
                f"Vol: {self.volumen_m3}m³ | Peso: {self.peso_kg}kg | "
                f"Dest: {self.destino_nombre} ({self.lat}, {self.lon})>")
