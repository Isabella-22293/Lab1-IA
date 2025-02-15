from search import bfs, dfs, uniform_cost_search, a_star_search, greedy_best_first_search
from node import Node
from queues import QueueFIFO, QueueLIFO, PriorityQueue

# Datos de costos 
costs = {
    "Warm-up activities": [("Skipping Rope", 10), ("Exercise bike", 10), ("Tread Mill", 10), ("Step Mill", 10)],
    "Skipping Rope": [("Dumbbell", 15), ("Barbell", 15)],
    "Exercise bike": [("Cable-Crossover", 25)],
    "Tread Mill": [("Pulling Bars", 20), ("Incline Bench", 20)],
    "Step Mill": [("Incline Bench", 16)],
    "Dumbbell": [("Leg Press Machine", 12)],
    "Barbell": [("Leg Press Machine", 10)],
    "Cable-Crossover": [("Climbing Rope", 10)],
    "Pulling Bars": [("Climbing Rope", 6)],
    "Incline Bench": [("Hammer Strength", 20)],
    "Leg Press Machine": [("Stretching", 11)],
    "Climbing Rope": [("Stretching", 10)],
    "Hammer Strength": [("Stretching", 8)]
}

# Datos heurísticos 
heuristics = {
    "Warm-up activities": 5, "Skipping Rope": 16, "Exercise bike": 10, "Tread Mill": 12,
    "Step Mill": 14, "Dumbbell": 9, "Barbell": 10, "Cable-Crossover": 8, "Pulling Bars": 10,
    "Incline Bench": 8, "Leg Press Machine": 8, "Climbing Rope": 5, "Hammer Strength": 4,
    "Stretching": 0
}

def run_searches(start, goal):
    print("\nBFS:")
    print(bfs(start, goal, costs))

    print("\nDFS:")
    print(dfs(start, goal, costs))

    print("\nUniform Cost Search:")
    print(uniform_cost_search(start, goal, costs))

    print("\nA* Search:")
    print(a_star_search(start, goal, costs, heuristics))

    print("\nGreedy Best-First Search:")
    print(greedy_best_first_search(start, goal, costs, heuristics))

if __name__ == "__main__":
    start_node = "Warm-up activities"
    goal_node = "Stretching"
    run_searches(start_node, goal_node)
