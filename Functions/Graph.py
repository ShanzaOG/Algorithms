"""
A graph is a collection of nodes (vertices) and edges that connect pairs of nodes.
Graphs can be used to represent various relationships and structures in real-world problems.
"""


class Graph:
    def __init__(self):
        # Initialize an empty dictionary to represent the graph
        self.vertices = {}

    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it doesn't already exist
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, start_vertex, end_vertex):
        # Add a directed edge from start_vertex to end_vertex
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex].append(end_vertex)
            # Uncomment the next line for an undirected graph
            # self.vertices[end_vertex].append(start_vertex)

    def print_graph(self):
        # Print each vertex and its list of adjacent vertices
        for vertex, edges in self.vertices.items():
            print(f"{vertex}: {edges}")
