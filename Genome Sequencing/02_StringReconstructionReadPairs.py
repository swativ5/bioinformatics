"""
Code Challenge: Solve the String Reconstruction from Read-Pairs Problem.
    Input: Integers k and d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.

To solve the String Reconstruction from Read-Pairs Problem, you will need to reconstruct a string from its path in the paired de Bruijn graph. Check out Charging Station: Reconstructing a String in the Paired de Bruijn Graph to see how this can be done.

Sample Input:
4 2
GAGA|TTGA TCGT|GATG CGTG|ATGT TGGT|TGAG GTGA|TGTT GTGG|GTGA TGAG|GTTG GGTC|GAGA GTCG|AGAT

Sample Output:
GTGGTCGTGAGATGTTGA
"""
import random

def prefix(text):
    return text[:-1]

def suffix(text):
    return text[1:]

def modifiedDeBruijnKmers(paired_kmers):
    graph = {}
    for pair in paired_kmers:
        kmer1, kmer2 = pair
        p1, s1 = prefix(kmer1), suffix(kmer1)
        p2, s2 = prefix(kmer2), suffix(kmer2)
        key = (p1, p2)
        value = (s1, s2)
        graph.setdefault(key, []).append(value)
    return graph

def formCycle(graph, node):
    cycle = []
    stack = [node]
    edges = {node : 0 for node in graph}

    while stack:
        node = stack[-1]

        if node in graph and edges.get(node, 0) < len(graph.get(node, [])):
            next_node = graph[node][edges[node]]
            edges[node] += 1
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    cycle = cycle[::-1]
    incomplete_nodes = [node for node in cycle if edges.get(node, 0) < len(graph.get(node, []))]

    return cycle, incomplete_nodes

def modifiedEulerianCycle(graph, startNode):
    cycle, incomplete_explored_nodes = formCycle(graph, startNode)

    while incomplete_explored_nodes:
        n = random.randint(0, len(incomplete_explored_nodes)- 1)
        newStart = incomplete_explored_nodes[n]
        ncycle, _ = formCycle(graph, newStart)

        index = cycle.index(newStart)
        cycle = cycle[:index] + ncycle + cycle[index + 1:]

        incomplete_explored_nodes = []
        for node in cycle:
            for next_node in graph[node]:
                if next_node not in cycle:
                    incomplete_explored_nodes.append(node)
    return cycle

def modifiedEulerianPath(graph):
    all_nodes = set(graph.keys()).union(*graph.values())
    indegree = {node: 0 for node in all_nodes}
    outdegree = {node: 0 for node in all_nodes}

    for key in graph.keys():
        for value in graph.get(key, []):
            indegree[value] += 1
            outdegree[key] += 1

    startNode, endNode = None, None
    for node in all_nodes:
        if outdegree[node] == indegree[node] + 1:
            startNode = node
        elif indegree[node] == outdegree[node] + 1:
            endNode = node

    if startNode is None:
        startNode = next(iter(graph))

    return modifiedEulerianCycle(graph, startNode)

def modifiedGenomePath(k, d, path):
    prefix_string = path[0][0]
    suffix_string = path[0][1]
    for pair in path[1:]:
        prefix_string += pair[0][-1]
        suffix_string += pair[1][-1]
    return prefix_string + suffix_string[-(k + d):]

def StringReconstructionReadPairs(k, d, Patterns):
    dB = modifiedDeBruijnKmers(Patterns)
    path = modifiedEulerianPath(dB)
    Text = modifiedGenomePath(k, d, path)
    return Text

def parsing(text):
    lines = text.strip().split("\n")
    header = lines[0].split()
    k = int(header[0])
    d = int(header[1])
    paired_reads = []
    for kmer in lines[1].split():
        pair = tuple(kmer.split("|"))
        paired_reads.append(pair)
    return k, d, paired_reads

if __name__ == "__main__":
    for i in range(5):
        file_input = open(f"StringReconstructionReadPairs/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        k, d, Patterns = parsing(file_input_text)

        file_output = open(f"StringReconstructionReadPairs/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_output = StringReconstructionReadPairs(k, d, Patterns)

        if file_output_text == f_output:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_output)

    file_input = open(f"/home/swativ5/Downloads/dataset_30188_16.txt")
    file_input_text = file_input.read()
    k, d, Patterns = parsing(file_input_text)
    f_output = StringReconstructionReadPairs(k, d, Patterns)
    f = open("test.txt", "w")
    f.write(f_output)
