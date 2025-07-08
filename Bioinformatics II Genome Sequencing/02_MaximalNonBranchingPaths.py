"""
Code Challenge: Implement MaximalNonBranchingPaths.
    Input: The adjacency list of a graph whose nodes are integers.
    Output: The collection of all maximal nonbranching paths in this graph.

Sample Input:
1: 2
2: 3
3: 4 5
6: 7
7: 6

Sample Output:
1 2 3
3 4
3 5
7 6 7

MaximalNonBranchingPaths(Graph)
    Paths ← empty list
    for each node v in Graph
        if v is not a 1-in-1-out node
            if out(v) > 0
                for each outgoing edge (v, w) from v
                    NonBranchingPath ← the path consisting of single edge (v, w)
                    while w is a 1-in-1-out node
                        extend NonBranchingPath by the edge (w, u)
                        w ← u
                    add NonBranchingPath to the set Paths
    for each isolated cycle Cycle in Graph
        add Cycle to Paths
    return Paths
"""

def MaximalNonBranchingPaths(Graph):
    Paths = []
    nodes1in1out = set()
    nExplored = set()

    all_nodes = set(Graph.keys()).union(*Graph.values())
    indegree = {node: 0 for node in all_nodes}
    outdegree = {node: 0 for node in all_nodes}

    for key in Graph.keys():
        for value in Graph.get(key, []):
            indegree[value] += 1
            outdegree[key] += 1

    for node_v in Graph.keys():
        if not (indegree[node_v] == 1 and outdegree[node_v] == 1):
            if outdegree[node_v] > 0:
                for node_w in Graph[node_v]:
                    NonBranchingPath = [node_v, node_w]
                    while (indegree[node_w] == 1 and outdegree[node_w] == 1):
                        nExplored.add(node_w)
                        node_u = Graph[node_w][0]
                        NonBranchingPath.append(node_u)
                        node_w = node_u
                    Paths.append(NonBranchingPath)
        else:
            nodes1in1out.add(node_v)

    for node_v in nodes1in1out:
        if node_v not in nExplored:
            node_w = node_v
            nbPath = []
            while node_w in nodes1in1out:
                nbPath.append(node_w)
                if node_w == node_v and len(nbPath) > 1:
                    Paths.append(nbPath)
                    for node in nbPath:
                        nExplored.add(node)
                    break
                node_w = Graph[node_w][0]

    # for node in Graph:
    #     if indegree[node] == 1 and outdegree[node] == 1:
    #         cycle = []
    #         current = node

    #         while current in Graph and Graph[current]:
    #             cycle.append(current)
    #             next_node = Graph[current][0]

    #             if next_node == node:
    #                 cycle.append(next_node)
    #                 break
    #             current = next_node

    #         if cycle not in Paths:
    #             Paths.append(cycle)

    s = ""
    for line in Paths:
        s += " ".join(map(str, line))
        s += "\n"
    return s

def parsing(text):
    Graph = {}
    for line in text.strip().split("\n"):
        node, neighbors = line.split(":")
        node = int(node.strip())
        neighbors = list(map(int, neighbors.strip().split()))
        Graph[node] = neighbors
    return Graph

if __name__ == "__main__":
    for i in range(6):
        file_input = open(f"MaximalNonBranchingPaths/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        Graph = parsing(file_input_text)

        file_output = open(f"MaximalNonBranchingPaths/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_output = MaximalNonBranchingPaths(Graph)

        if file_output_text == f_output:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_output)

    file_input = open(f"/home/swativ5/Downloads/dataset_30188_16.txt")
    file_input_text = file_input.read()
    Graph = parsing(file_input_text)
    f_output = MaximalNonBranchingPaths(Graph)
    f = open("test.txt", "w")
    f.write(f_output)
