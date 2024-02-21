'''
NAME: BARECHA ASHENAFI
ID: 0546/13
COURSE_CODE: SEng4081
'''

from collections import deque
# imports the deque class from the collections module in Python.
class Graph:
    def __init__(self):
        # Initialize an empty graph represented as an adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge to the graph
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_node):
        # Perform breadth-first search starting from the specified node
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start_node])  # Use a deque as a queue for BFS

        while queue:
            current_node = queue.popleft()  # Dequeue the front node
            if current_node not in visited:
                print(f"Visiting node {current_node}")
                visited.add(current_node)  # Mark the current node as visited

                if current_node in self.graph:
                    # Enqueue neighbors of the current node
                    queue.extend(self.graph[current_node])
                    print(f"  Enqueuing neighbors {self.graph[current_node]}")


# Example usage:
if __name__ == "__main__":
    # Create a graph and add edges
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    # Perform breadth-first search starting from node 1
    print("Breadth-First Search starting from node 1:")
    g.bfs(1)
