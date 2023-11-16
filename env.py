import pandas as pd
import networkx as nx

# Load the latest dataset
file = './data.xlsx'
data = pd.read_excel(file)

# Initialize graph
G = nx.Graph()


def generate(datafile, graph):
    for index, row in datafile.iterrows():
        # Node will be named after 'city, state'
        node_name = f"{row['city']}, {row['state']}"
        # Parse lists
        connected_cities = row['connected cities'].split(',')
        connected_states = row['connected cities states'].split(',')
        distances = [int(dist) for dist in row['distance to city'].split(',')]

        # Add the current city if not already in graph or update with lat, long, & interstates
        graph.add_node(node_name, lat=row['lat'], long=row['long'], interstates=row['interstates'])

        # Add edges
        for i, (connected_city, connected_state) in enumerate(zip(connected_cities, connected_states)):
            connected_city_state = f"{connected_city.strip()}, {connected_state.strip()}"
            if connected_city_state not in graph:
                graph.add_node(connected_city_state)
            # Distance is cost
            graph.add_edge(node_name, connected_city_state, distance=distances[i])


generate(data, G)

nodes = G.number_of_nodes()
edges = G.number_of_edges()
print("nodes: ", nodes, " | edges: ", edges)
# print(G)
# for line in nx.generate_adjlist(G):
#     print(line)