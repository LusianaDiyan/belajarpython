from collections import defaultdict

distance = []

class Graph():
    def _init_(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    #menambahkan node dari asal ke tujuan
    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()

#inisialisasi weight tiap edge
edges = [
     ('H', 'G', 449),
     ('G', 'H', 449),
     ('F', 'C', 669),
     ('C', 'F', 669),
     ('C', 'D', 480),
     ('D', 'C', 480),
     ('E', 'D', 733),
     ('D', 'E', 733),
     ('D', 'D', 94),
     ('Z', 'A', 909),
     ('A', 'Z', 909),
     ('Z', 'D', 1215),
     ('D', 'Z', 1215),
     ('E', 'G', 482),
     ('G', 'E', 482),
     ('H', 'G', 453),
     ('G', 'H', 453),
     ('B', 'Z', 1390),
     ('Z', 'B', 1390),
     ('E', 'E', 381),
     ('C', 'A', 1517),
     ('A', 'C', 1390),
]

#looping input node asal ke tujuan
for edge in edges:
    graph.add_edge(*edge)


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    #memasukkan current node ke dalam visited
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node] #memasukkan node pada graph
        weight_to_current_node = shortest_paths[current_node][1]


        for next_node in destinations:
            #menambahkan weight dari current node
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            #menambahkan current node ke shortest paths
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                #membandingkan weight terpendek
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        distance.append(weight)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

print("Shortest Path : ")
print(dijsktra(graph, 'A', 'Z'))
for x in distance:
    temp = 0
    temp = temp + x
    harga = temp * 10
    print("Distance : ")
    print(temp, "meter")
    print("Harga : ")
    print("Rp ", harga)
    break