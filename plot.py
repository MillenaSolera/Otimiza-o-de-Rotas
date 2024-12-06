import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:
    def __init__(self):
        # Inicializa o grafo
        self.G = nx.Graph()

    def add_nodes(self, nodes):
        """Add nodes to the graph."""
        self.G.add_nodes_from(nodes)

    def add_node(self, node, coordenadas=None, warehouse=False):
        """Add node to the graph with optional coordinates as an attribute."""
        if coordenadas and warehouse:
            
            self.G.add_node(node, coordenadas=coordenadas, warehouse=warehouse)
        elif coordenadas:
             
            self.G.add_node(node, coordenadas=coordenadas)
        else:
            
            self.G.add_node(node)

    def add_edges(self, edges):
        """Adiciona as arestas."""
        self.G.add_edges_from(edges)

    def add_edge(self, node1, node2, weight=None, attributes=None):
        """Adiciona aresta entre dois nós com peso opcional e atributos adicionais."""
        if attributes is None:
            attributes = {}

        if weight is not None:
            attributes['weight'] = weight

        self.G.add_edge(node1, node2, **attributes)

    def display(self):

        plt.figure(figsize=(12, 12))

        pos = {}

        for node in self.G.nodes():
            if 'coordenadas' in self.G.nodes[node]:
                lat, lon = self.G.nodes[node]['coordenadas'].split(', ')
                lat, lon = float(lat), float(lon)
                
                
                pos[node] = (lon, lat)  # Longitude é x, Latitude é y
        
        
        node_colors = []
        for node in self.G.nodes():
            if 'warehouse' in self.G.nodes[node]:
                node_colors.append('red')  
            else:
                node_colors.append('lightblue') 

        nx.draw_networkx_nodes(self.G, pos, node_color=node_colors, node_size=300)
        nx.draw_networkx_labels(self.G, pos, font_size=6, font_weight='bold', font_color='black')
        nx.draw_networkx_edges(self.G, pos, edge_color='gray', width=1)

        plt.title('Brazil Warehouses & Cities')
        plt.axis('off')  
        plt.show()