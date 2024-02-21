'''
NAME: BARECHA ASHENAFI
ID: 0546/13
COURSE_CODE: SEng4081
'''

import heapq  # provides functions for creating and manipulating heaps

class Graph:
    def __init__(self):
        # Initialize an empty graph represented as an adjacency list
        self.graph = {}

    def add_edge(self, u, v, weight):
        # Add an edge to the graph with a given weight
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def best_first_search(self, start_node, goal_node):
        visited = set()
        priority_queue = [(0, start_node)]  # Priority queue with initial cost and node
        while priority_queue:
            cost, current_node = heapq.heappop(priority_queue)  # Pop node with the lowest cost
            if current_node not in visited:
                print(f"Visiting node {current_node}")
                visited.add(current_node)

                if current_node == goal_node:
                    print("Goal node reached!")
                    return

                if current_node in self.graph:
                    # Enqueue neighbors with their heuristic values as priorities
                    for neighbor, weight in self.graph[current_node]:
                        heapq.heappush(priority_queue, (weight, neighbor))

# Example usage:
if __name__ == "__main__":
    # Create a graph and add edges with weights
    g = Graph()
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 4, 1)
    g.add_edge(2, 5, 7)
    g.add_edge(3, 6, 2)
    g.add_edge(3, 7, 4)

    # Perform Best-First Search from node 1 to node 7
    print("Best-First Search from node 1 to node 7:")
    g.best_first_search(1, 7)
