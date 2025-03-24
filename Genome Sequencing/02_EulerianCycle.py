"""
EulerianCycle(Graph)
    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
        Cycle ← Cycle’
    return Cycle

Code Challenge: Solve the Eulerian Cycle Problem.
         Input: The adjacency list of an Eulerian directed graph.
         Output: An Eulerian cycle in this graph.

Sample Input:
0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6

Sample Output:
6 8 7 9 6 5 4 2 1 0 3 2 6
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

def EulerianCycle(graph):
    start = list(graph.keys())[0]
    cycle, incomplete_explored_nodes = formCycle(graph, start)

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

def parsing(text):
    graph = {}
    text = text.strip().split("\n")
    for item in text:
        key, value = item.split(": ")
        values = value.split()
        graph[int(key)] = [int(value) for value in values]
    return graph

if __name__ == "__main__":
    for i in range(7):
        file_input = open(f"EulerianCycle/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        graph = parsing(file_input_text)

        file_output = open(f"EulerianCycle/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_cycle = " ".join(str(element) for element in EulerianCycle(graph))

        if file_output_text == f_cycle:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_cycle)

    file_input = open(f"/home/swativ5/Downloads/dataset_30187_2.txt")
    file_input_text = file_input.read()
    graph = parsing(file_input_text)
    f_cycle = " ".join(str(element) for element in EulerianCycle(graph))
    f = open("test.txt", "w")
    f.write(f_cycle)
