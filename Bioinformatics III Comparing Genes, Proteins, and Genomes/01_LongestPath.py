'''
Code Challenge: Solve the Longest Path in a DAG Problem.
    Input: An integer representing the starting node to consider in a graph, 
        followed by an integer representing the ending node to consider, 
        followed by a list of edges in the graph. 
        The edge notation "0 1 7" indicates that an edge connects node 0 to node 1 with weight 7.  
        You may assume a given topological order corresponding to nodes in increasing order.
    Output: The length of a longest path in the graph, 
    followed by a longest path as a sequence of space-separated node labels. 
    (If multiple longest paths exist, you may return any one.)

Sample Input:
0 4
0 1 7
0 2 4
2 3 2
1 4 1
3 4 3

Sample Output:
9
0 2 3 4
'''

def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]

def LongestPath(graph, start, end):
    ordered = topological_sort(graph)
    distances = {node: float('-inf') for node in graph}
    distances[start] = 0
    parents = {node: None for node in graph}

    for node in ordered:
        if distances[node] != float('-inf'):
            for neighbor, weight in graph.get(node, []):
                if distances[neighbor] < distances[node] + weight:
                    distances[neighbor] = distances[node] + weight
                    parents[neighbor] = node
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    
    return distances[end], path

if __name__ == "__main__":
    for i in range(1, 8):
        file_input = open(f"/home/swativ5/Downloads/LongestPath/inputs/input_{i}.txt", "r")
        file_input_text = file_input.read()
        input_data = file_input_text.strip().split('\n')
        start, end = map(int, input_data[0].split())
        edges = [list(map(int, line.split())) for line in input_data[1:]]
        
        graph = {}
        for u, v, w in edges:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
            if v not in graph:
                graph[v] = []
        
        length, path = LongestPath(graph, start, end)
        file_output = open(f"/home/swativ5/Downloads/LongestPath/outputs/output_{i}.txt", "r")
        file_output_text = file_output.read()
        if file_output_text.strip() == str(length) + '\n' + ' '.join(map(str, path)):
            print("Correct")
        else:
            print("Wrong")
            print("Expected:", file_output_text.strip())
            print("Got:", str(length) + '\n' + ' '.join(map(str, path)))

    file_input = open("/home/swativ5/Downloads/dataset_30197_7.txt", "r")
    file_input_text = file_input.read()
    input_data = file_input_text.strip().split('\n')
    start, end = map(int, input_data[0].split())
    edges = [list(map(int, line.split())) for line in input_data[1:]]
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))
        if v not in graph:
            graph[v] = []
    length, path = LongestPath(graph, start, end)
    f = open("test.txt", "w")
    f.write(str(length) + '\n' + ' '.join(map(str, path)))