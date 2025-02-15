from collections import deque

class QueueFIFO:
    def __init__(self):
        self.elements = deque()

    def EMPTY(self):
        return len(self.elements) == 0

    def TOP(self):
        # Retorna el primer elemento sin removerlo
        return self.elements[0] if not self.EMPTY() else None

    def POP(self):
        # Retorna y remueve el primer elemento
        return self.elements.popleft() if not self.EMPTY() else None

    def ADD(self, item):
        # Inserta al final de la cola
        self.elements.append(item)
        return self.elements
class QueueLIFO:
    def __init__(self):
        self.elements = []

    def EMPTY(self):
        return len(self.elements) == 0

    def TOP(self):
        # Retorna el último elemento sin removerlo
        return self.elements[-1] if not self.EMPTY() else None

    def POP(self):
        # Retorna y remueve el último elemento
        return self.elements.pop() if not self.EMPTY() else None

    def ADD(self, item):
        # Inserta al final (top) de la pila
        self.elements.append(item)
        return self.elements
import heapq

class PriorityQueue:
    def __init__(self):
        # Cada elemento será una tupla (priority, item)
        self.elements = []

    def EMPTY(self):
        return len(self.elements) == 0

    def TOP(self):
        # Retorna el nodo con menor prioridad sin removerlo
        return self.elements[0][1] if not self.EMPTY() else None

    def POP(self):
        # Extrae el nodo con menor prioridad 
        if self.EMPTY():
            return None
        _, node = heapq.heappop(self.elements)
        return node

    def ADD(self, item, priority=0):
        # Inserta un elemento con su prioridad
        heapq.heappush(self.elements, (priority, item))
        return self.elements
