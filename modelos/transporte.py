class VehiculoTransporte:
    """Clase base para cualquier medio de transporte"""
    def __init__(self, id_vehiculo, nombre, tipo, capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh):
        self.id_vehiculo = id_vehiculo
        self.nombre = nombre
        self.tipo = tipo  # 'barco', 'avion', 'furgon', 'van', 'moto'
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
        """Verifica si el paquete cabe tanto en peso como en volumen"""
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
        return (f"<{self.nombre} ({self.tipo}) | Carga: {self.peso_actual_kg}/{self.capacidad_peso_kg}kg "
                f"({self.porcentaje_peso_usado}%) | Vol: {self.volumen_actual_m3}/{self.capacidad_volumen_m3}m³ "
                f"({self.porcentaje_volumen_usado}%) | Paquetes: {len(self.paquetes_asignados)}>")


class BarcoCarga(VehiculoTransporte):
    """Barcos de transporte de carga: Puerto a Puerto (gran volumen y peso)"""
    def __init__(self, id_vehiculo="BAR-01", nombre="Buque Portacontenedores Tolima", 
                 capacidad_peso_kg=60000, capacidad_volumen_m3=450):
        super().__init__(id_vehiculo, nombre, "barco", capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=40.0)


class AvionCarga(VehiculoTransporte):
    """Aviones de transporte: País a País (rápido, prioridad alta, capacidad moderada)"""
    def __init__(self, id_vehiculo="AV-01", nombre="Boeing 777F Cargo Express", 
                 capacidad_peso_kg=18000, capacidad_volumen_m3=110):
        super().__init__(id_vehiculo, nombre, "avion", capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=850.0)


class FurgonTerrestre(VehiculoTransporte):
    """Furgón para distribución terrestre en Ibagué: Cargas pesadas e industriales"""
    def __init__(self, id_vehiculo="FUR-01", nombre="Furgón Distribución Ibagué (Chevrolet FTR)", 
                 capacidad_peso_kg=4000, capacidad_volumen_m3=22):
        super().__init__(id_vehiculo, nombre, "furgon", capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=45.0)


class VanTerrestre(VehiculoTransporte):
    """Van para distribución terrestre en Ibagué: Cargas medianas y comerciales"""
    def __init__(self, id_vehiculo="VAN-01", nombre="Van Urbana Ibagué (Renault Master)", 
                 capacidad_peso_kg=1200, capacidad_volumen_m3=9):
        super().__init__(id_vehiculo, nombre, "van", capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=40.0)


class MotoTerrestre(VehiculoTransporte):
    """Moto para distribución terrestre en Ibagué: Mensajería rápida y paquetes pequeños"""
    def __init__(self, id_vehiculo="MOT-01", nombre="Moto Reparto Ibagué (Yamaha Cargo)", 
                 capacidad_peso_kg=35, capacidad_volumen_m3=0.3):
        super().__init__(id_vehiculo, nombre, "moto", capacidad_peso_kg, capacidad_volumen_m3, velocidad_promedio_kmh=35.0)
