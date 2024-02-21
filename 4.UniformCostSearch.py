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

    def add_edge(self, u, v, cost):
        # Add an edge to the graph with a given cost
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))

    def uniform_cost_search(self, start_node, goal_node):
        visited = set()
        priority_queue = [(0, start_node, [])]  # Priority queue with initial cost, node, and path
        while priority_queue:
            cost, current_node, path = heapq.heappop(priority_queue)  # Pop node with the lowest cost
            if current_node not in visited:
                print(f"Visiting node {current_node} with cost {cost}")
                visited.add(current_node)

                if current_node == goal_node:
                    print(f"Goal node reached with cost {cost}! Path: {path + [current_node]}")
                    return

                if current_node in self.graph:
                    # Enqueue neighbors with their cumulative costs and paths
                    for neighbor, edge_cost in self.graph[current_node]:
                        heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [current_node]))

# Example usage:
if __name__ == "__main__":
    # Create a graph and add edges with costs
    g = Graph()
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 4, 1)
    g.add_edge(2, 5, 7)
    g.add_edge(3, 6, 2)
    g.add_edge(3, 7, 4)

    # Perform Uniform Cost Search from node 1 to node 7
    print("Uniform Cost Search from node 1 to node 7:")
    g.uniform_cost_search(1, 7)
