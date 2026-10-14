from collections import deque

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

def bfs(raiz):
    if raiz is None:
        return []
    cola = deque([raiz])
    resultado = []
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izquierdo:
            cola.append(nodo.izquierdo)
        if nodo.derecho:
            cola.append(nodo.derecho)
    return resultado

bst = ArbolBinarioBusqueda()
for v in [10, 5, 15, 2, 7]:
    bst.insertar(v)

print("Recorrido BFS:", bfs(bst.raiz))





