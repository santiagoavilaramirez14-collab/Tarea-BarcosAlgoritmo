# Arbol Binario de Busqueda (BST) para organizar los paquetes en bodega por ID


class NodoBST:
    def __init__(self, paquete):
        self.paquete = paquete
        self.id_paquete = paquete.id_paquete
        self.izquierda = None
        self.derecha = None


class ArbolBodega:
    """
    Organización en almacén/bodega por ID de paquete o prioridad.
    Permite inserciones y búsquedas eficientes en tiempo O(log n).
    """
    def __init__(self):
        self.raiz = None
        self.total_paquetes = 0

    def insertar(self, paquete):
        self.raiz = self._insertar(self.raiz, paquete)
        self.total_paquetes += 1

    def _insertar(self, nodo, paquete):
        if nodo is None:
            return NodoBST(paquete)

        if paquete.id_paquete < nodo.id_paquete:
            nodo.izquierda = self._insertar(nodo.izquierda, paquete)
        elif paquete.id_paquete > nodo.id_paquete:
            nodo.derecha = self._insertar(nodo.derecha, paquete)
        else:
            # Si el ID ya existe, actualizamos los datos
            nodo.paquete = paquete
        return nodo

    def buscar_paquete(self, id_paquete):
        return self._buscar(self.raiz, id_paquete)

    def _buscar(self, nodo, id_paquete):
        if nodo is None or nodo.id_paquete == id_paquete:
            return nodo.paquete if nodo else None

        if id_paquete < nodo.id_paquete:
            return self._buscar(nodo.izquierda, id_paquete)
        return self._buscar(nodo.derecha, id_paquete)

    def inorden(self):
        """Retorna todos los paquetes en orden ascendente por su ID"""
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, lista):
        if nodo is not None:
            self._inorden(nodo.izquierda, lista)
            lista.append(nodo.paquete)
            self._inorden(nodo.derecha, lista)
