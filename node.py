class Node:
    
    #Estructura de nodo para búsqueda.
    #state: nombre de la actividad 
    #parent: referencia al nodo padre
    #path_cost: costo acumulado g(n)
    #heuristic: valor heurística h(n)

    def __init__(self, state, parent=None, path_cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost   
        self.heuristic = heuristic   

    def __lt__(self, other):
        #Comparar nodos en la PriorityQueue A*.
        #Se compara f(n) = g(n) + h(n).
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)
