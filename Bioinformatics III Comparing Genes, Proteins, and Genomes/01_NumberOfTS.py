import copy

def build_graph(adjacency_list):
    graph = dict()
    for vertex, neighbors in adjacency_list.items():
        graph[vertex] = list(neighbors)
    return graph

def remove_vertex(graph, vertex):
    new_graph = copy.deepcopy(graph)
    if vertex in new_graph:
        del new_graph[vertex]
    for v in new_graph:
        if vertex in new_graph[v]:
            new_graph[v].remove(vertex)
    return new_graph

def find_sources(graph):
    all_vertices = set(graph.keys())
    all_neighbors = set()
    for neighbors in graph.values():
        for neighbor in neighbors:
            all_neighbors.add(neighbor)
    return all_vertices - all_neighbors

def count_topo_sorts(graph):
    if not graph:
        return 1
    total = 0
    sources = find_sources(graph)
    for source in sources:
        smaller_graph = remove_vertex(graph, source)
        total += count_topo_sorts(smaller_graph)
    return total

graph = {
    'tights': ['leotard', 'boots'],
    'leotard': ['shorts', 'cape', 'gloves'],
    'shorts': ['boots', 'belt'],
    'boots': [],
    'cape': ['hood'],
    'gloves': [],
    'belt': [],
    'hood': []
}

graph = build_graph(graph)
result = count_topo_sorts(graph)
print(result)
