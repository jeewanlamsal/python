
def create_weighted_graph():
    # Representing the graph as an adjacency list with weights
    graph = {
        'Biratnagar': {'Itahari': 22, 'Rangeli': 25},
        'Itahari': {'Biratnagar': 22, 'Biratchowk': 11, 'Dharan': 20},
        'Dharan': {'Itahari': 20},
        'Biratchowk': {'Itahari': 11, 'Kanepokhari': 10},
        'Rangeli': {'Biratnagar': 25, 'Kanepokhari': 25},
        'Kanepokhari': {'Biratchowk': 10, 'Rangeli': 25, 'Urlabari': 12},
        'Urlabari': {'Kanepokhari': 12, 'Damak': 6},
        'Damak': {'Urlabari': 6}
    }
    return graph

# Function to display the graph
def display_weighted_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(f'{neighbor} ({distance} km)' for neighbor, distance in neighbors.items())}")

# Creating and displaying the graph
weighted_graph = create_weighted_graph()
display_weighted_graph(weighted_graph)

