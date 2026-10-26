class VehiculoTransporte:
    """Clase base para el transporte de carga"""
    def __init__(self, id_vehiculo, nombre, capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=40.0):
        self.id_vehiculo = id_vehiculo
        self.nombre = nombre
        self.tipo = "barco"
        self.capacidad_peso_kg = float(capacidad_peso_kg)
        self.capacidad_volumen_m3 = float(capacidad_volumen_m3)
        self.velocidad_promedio_kmh = float(velocidad_promedio_kmh)
        self.paquetes_asignados = []

    @property
    def peso_actual_kg(self):
        return round(sum(p.peso_kg for p in self.paquetes_asignados), 2)

    @property
    def volumen_actual_m3(self):
        return round(sum(p.volumen_m3 for p in self.paquetes_asignados), 3)

    @property
    def porcentaje_peso_usado(self):
        if self.capacidad_peso_kg == 0: return 0.0
        return round((self.peso_actual_kg / self.capacidad_peso_kg) * 100, 2)

    @property
    def porcentaje_volumen_usado(self):
        if self.capacidad_volumen_m3 == 0: return 0.0
        return round((self.volumen_actual_m3 / self.capacidad_volumen_m3) * 100, 2)

    def puede_cargar(self, paquete):
        peso_ok = (self.peso_actual_kg + paquete.peso_kg) <= self.capacidad_peso_kg
        vol_ok = (self.volumen_actual_m3 + paquete.volumen_m3) <= self.capacidad_volumen_m3
        return peso_ok and vol_ok

    def cargar_paquete(self, paquete):
        if self.puede_cargar(paquete):
            self.paquetes_asignados.append(paquete)
            return True
        return False

    def vaciar_carga(self):
        self.paquetes_asignados = []

    def __repr__(self):
        return (f"<{self.nombre} | Peso: {self.peso_actual_kg}/{self.capacidad_peso_kg}kg "
                f"({self.porcentaje_peso_usado}%) | Vol: {self.volumen_actual_m3}/{self.capacidad_volumen_m3}m³ "
                f"({self.porcentaje_volumen_usado}%) | Paquetes: {len(self.paquetes_asignados)}>")


class BarcoCarga(VehiculoTransporte):
    # Barco para rutas puerto a puerto
    def __init__(self, id_vehiculo="BAR-01", nombre="Barco Portacontenedores", 
                 capacidad_peso_kg=35000, capacidad_volumen_m3=250):
        super().__init__(id_vehiculo, nombre, capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=40.0)
