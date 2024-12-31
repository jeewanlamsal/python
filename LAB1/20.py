#WAP to represent the following graphs using a dictionary.

def create_graph():
    # Representing the graph as an adjacency list using a dictionary
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': ['H'],
        'F': [],
        'G': [],
        'H': []
    }
    return graph

# Function to display the graph
def display_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors) if neighbors else 'No neighbors'}")

# Creating and displaying the graph
graph = create_graph()
display_graph(graph)