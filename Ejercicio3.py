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

def suma_nodos(nodo):
    if nodo is None:
        return 0
    return nodo.valor + suma_nodos(nodo.izquierdo) + suma_nodos(nodo.derecho)

bst = ArbolBinarioBusqueda()
for v in [10, 5, 15]:
    bst.insertar(v)

print("Suma de elementos:", suma_nodos(bst.raiz))

