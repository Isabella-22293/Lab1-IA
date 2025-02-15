from node import Node
from queues import QueueFIFO, QueueLIFO, PriorityQueue

def reconstruct_path(node):
    #Reconstruye el camino desde el nodo final hasta el inicio 
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def bfs(start, goal, graph):
    #BFS
    queue = QueueFIFO()
    queue.ADD(Node(start))
    visited = set()

    while not queue.EMPTY():
        node = queue.POP()
        if node.state in visited:
            continue
        visited.add(node.state)

        if node.state == goal:
            return reconstruct_path(node)

        for neighbor, cost in graph.get(node.state, []):
            queue.ADD(Node(neighbor, parent=node))

    return None  

def dfs(start, goal, graph):
    #(DFS) 
    stack = QueueLIFO()
    stack.ADD(Node(start))
    visited = set()

    while not stack.EMPTY():
        node = stack.POP()
        if node.state in visited:
            continue
        visited.add(node.state)

        if node.state == goal:
            return reconstruct_path(node)

        for neighbor, cost in graph.get(node.state, []):
            stack.ADD(Node(neighbor, parent=node))

    return None

def uniform_cost_search(start, goal, graph):
    #(UCS)
    queue = PriorityQueue()
    queue.ADD(Node(start, path_cost=0), priority=0)
    visited = {}

    while not queue.EMPTY():
        node = queue.POP()
        if node.state in visited and visited[node.state] <= node.path_cost:
            continue
        visited[node.state] = node.path_cost

        if node.state == goal:
            return reconstruct_path(node)

        for neighbor, cost in graph.get(node.state, []):
            total_cost = node.path_cost + cost
            queue.ADD(Node(neighbor, parent=node, path_cost=total_cost), priority=total_cost)

    return None

def a_star_search(start, goal, graph, heuristics):
    #Búsqueda A* 
    queue = PriorityQueue()
    queue.ADD(Node(start, path_cost=0, heuristic=heuristics.get(start, 0)), priority=0)
    visited = {}

    while not queue.EMPTY():
        node = queue.POP()
        if node.state in visited and visited[node.state] <= node.path_cost:
            continue
        visited[node.state] = node.path_cost

        if node.state == goal:
            return reconstruct_path(node)

        for neighbor, cost in graph.get(node.state, []):
            g = node.path_cost + cost
            h = heuristics.get(neighbor, 0)
            f = g + h
            queue.ADD(Node(neighbor, parent=node, path_cost=g, heuristic=h), priority=f)

    return None

def greedy_best_first_search(start, goal, graph, heuristics):
    #Búsqueda Greedy Best-First
    queue = PriorityQueue()
    queue.ADD(Node(start, heuristic=heuristics.get(start, 0)), priority=heuristics.get(start, 0))
    visited = set()

    while not queue.EMPTY():
        node = queue.POP()
        if node.state in visited:
            continue
        visited.add(node.state)

        if node.state == goal:
            return reconstruct_path(node)

        for neighbor, cost in graph.get(node.state, []):
            h = heuristics.get(neighbor, 0)
            queue.ADD(Node(neighbor, parent=node, heuristic=h), priority=h)

    return None
