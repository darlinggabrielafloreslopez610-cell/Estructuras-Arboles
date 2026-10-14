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

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecho, resultado)

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

def balancear(lista):
    if not lista:
        return None
    medio = len(lista)//2
    nodo = NodoArbol(lista[medio])
    nodo.izquierdo = balancear(lista[:medio])
    nodo.derecho = balancear(lista[medio+1:])
    return nodo

bst = ArbolBinarioBusqueda()
for v in [1, 2, 3, 4, 5]:
    bst.insertar(v)

print("Árbol degenerado inorden:", bst.inorden())
nuevo_raiz = balancear(bst.inorden())
print("Árbol balanceado BFS:", bfs(nuevo_raiz))

