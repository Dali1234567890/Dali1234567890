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

    def a_star_search(self, start_node, goal_node, heuristic):
        visited = set()
        priority_queue = [(0 + heuristic(start_node, goal_node), 0, start_node, [])]
        while priority_queue:
            _, cost, current_node, path = heapq.heappop(priority_queue)
            if current_node not in visited:
                print(f"Visiting node {current_node} with cost {cost}")
                visited.add(current_node)

                if current_node == goal_node:
                    print(f"Goal node reached with total cost {cost}! Path: {path + [current_node]}")
                    return

                if current_node in self.graph:
                    for neighbor, edge_cost in self.graph[current_node]:
                        heapq.heappush(priority_queue, (cost + edge_cost + heuristic(neighbor, goal_node), cost + edge_cost, neighbor, path + [current_node]))

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

    # Define a heuristic function (for simplicity, using the absolute difference of node values)
    def heuristic(node, goal_node):
        return abs(node - goal_node)

    # Perform A* search from node 1 to node 7
    print("A* Search from node 1 to node 7:")
    g.a_star_search(1, 7, heuristic)
