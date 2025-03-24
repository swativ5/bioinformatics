"""
Code Challenge: Solve the String Reconstruction Problem.
    Input: An integer k followed by a list of k-mers Patterns.
    Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)


Sample Input:
4
CTTA ACCA TACC GGCT GCTT TTAC

Sample Output:
GGCTTACCA

StringReconstruction(Patterns)
    dB ← DeBruijn(Patterns)
    path ← EulerianPath(dB)
    Text﻿ ← PathToGenome(path)
    return Text
"""

def prefix(text):
    return text[:-1]

def suffix(text):
    return text[1:]

def DeBruijnKmers(kmers):
    graph = {}
    for kmer in kmers:
        p, s = prefix(kmer), suffix(kmer)
        graph.setdefault(p, []).append(s)
    return graph

def formCycle(graph, node):
    cycle = []
    stack = [node]
    edges = {node : 0 for node in graph}

    while stack:
        node = stack[-1]

        if edges.get(node, 0) < len(graph.get(node, [])):
            next_node = graph[node][edges[node]]
            edges[node] += 1
            stack.append(next_node)
        else:
            cycle.append(stack.pop())

    cycle = cycle[::-1]
    incomplete_nodes = [node for node in cycle if edges.get(node, 0) < len(graph.get(node, []))]

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

    return EulerianCycle(graph, startNode)

def GenomePath(kmers):
    sequence = kmers[0]
    for i in range(1, len(kmers)):
        sequence += kmers[i][-1]
    return sequence

def StringReconstruction(Patterns):
    dB = DeBruijnKmers(Patterns)
    path = EulerianPath(dB)
    Text = GenomePath(path)
    return Text

def parsing(text):
    k, text = text.strip().split("\n")
    kmers = [kmer for kmer in text.split()]
    return int(k), kmers

if __name__ == "__main__":
    for i in range(7):
        file_input = open(f"StringReconstruction/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        k, kmers = parsing(file_input_text)

        file_output = open(f"StringReconstruction/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_output = StringReconstruction(kmers)

        if file_output_text == f_output:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_output)

    file_input = open(f"/home/swativ5/Downloads/dataset_30187_7.txt")
    file_input_text = file_input.read()
    k, kmers = parsing(file_input_text)
    f_output = StringReconstruction(kmers)
    f = open("test.txt", "w")
    f.write(f_output)
