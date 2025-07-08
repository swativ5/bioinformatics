"""
Code Challenge: Solve the Eulerian Path Problem.
    Input: The adjacency list of a directed graph that has an Eulerian path.
    Output: An Eulerian path in this graph.

Sample Input:
0: 2
1: 3
2: 1
3: 0 4
6: 3 7
7: 8
8: 9
9: 6

Sample Output:
6 7 8 9 6 3 0 2 1 3 4
"""

def formCycle(graph, node):
    cycle = []
    stack = [node]
    edges = {node : 0 for node in graph}

    while stack:
        node = stack[-1]

        if edges[node] < len(graph[node]):
            next_node = graph[node][edges[node]]
            edges[node] += 1
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    cycle = cycle[::-1]
    incomplete_nodes = [node for node in cycle if edges[node] < len(graph[node])]

    return cycle, incomplete_nodes

def EulerianCycle(graph, startNode):
    cycle, incomplete_explored_nodes = formCycle(graph, startNode)

    while incomplete_explored_nodes:
        newStart = incomplete_explored_nodes[0]
        ncycle, incomplete_explored_nodes = formCycle(graph, newStart)

        index = cycle.index(newStart)
        cycle = cycle[:index] + ncycle + cycle[index + 1:]

        incomplete_explored_nodes = []
        for node in cycle:
            for next_node in graph[node]:
                if next_node not in cycle:
                    incomplete_explored_nodes.append(node)
    return cycle

def EulerianPath(graph):
    indegree = {node : 0 for node in graph}
    outdegree = {node : 0 for node in graph}

    for key in graph.keys():
        for value in graph.get(key, []):
            indegree[value] = indegree.get(value, 0) + 1
            outdegree[key] = outdegree.get(key, 0) + 1


    startNode, endNode = 0, 0
    for node in set(indegree.keys()).union(set(outdegree.keys())):
        if outdegree.get(node, 0) == indegree.get(node, 0) + 1:
            startNode = node
        # if outdegree[node] + 1 == indegree[node]:
        #     endNode = node
    return EulerianCycle(graph, startNode)

def parsing(text):
    graph = {}
    text = text.strip().split("\n")
    for item in text:
        key, value = item.split(": ")
        values = value.split()
        graph[int(key)] = [int(value) for value in values]
        for v in graph[int(key)]:
            if v not in graph:
                graph[v] = []
    return graph

if __name__ == "__main__":
    for i in range(6):
        file_input = open(f"EulerianPath/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        graph = parsing(file_input_text)

        file_output = open(f"EulerianPath/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_cycle = " ".join(str(element) for element in EulerianPath(graph))

        if file_output_text == f_cycle:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_cycle)

    file_input = open(f"/home/swativ5/Downloads/dataset_30187_6.txt")
    file_input_text = file_input.read()
    graph = parsing(file_input_text)
    f_cycle = " ".join(str(element) for element in EulerianPath(graph))
    f = open("test.txt", "w")
    f.write(f_cycle)
