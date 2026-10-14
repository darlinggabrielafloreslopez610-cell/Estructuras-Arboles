class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho, valor)
        else:
            # Caso 1: sin hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # Caso 2: un hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            # Caso 3: dos hijos
            sucesor = self._minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.valor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecho, resultado)

# Ejemplo
bst = ArbolBinarioBusqueda()
for v in [50, 30, 70, 20, 40, 60, 80]:
    bst.insertar(v)
print("Inorden antes de eliminar:", bst.inorden())
bst.eliminar(50)
print("Inorden después de eliminar 50:", bst.inorden())
