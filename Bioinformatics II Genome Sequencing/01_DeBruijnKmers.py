"""
DeBruijn(Patterns)
    dB ← graph in which every k-mer in Patterns is isolated edge between its prefix and suffix
    dB ← graph resulting from ﻿gluing all nodes in dB with identical labels
    return dB

DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
    Input: A collection of k-mers Patterns.
    Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

Code Challenge: Solve the de Bruijn Graph from k-mers Problem.

Sample Input:
GAGG CAGG GGGG GGGA CAGG AGGG GGAG

Sample Output:
AGG: GGG
CAG: AGG AGG
GAG: AGG
GGA: GAG
GGG: GGA GGG

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

if __name__ == "__main__":
    for i in range(5):
        file_input = open(f"DeBruijnKmers/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        kmers = file_input_text.strip().split()

        file_output = open(f"DeBruijnKmers/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip().split("\n")
        f_output_graph = {}
        for item in file_output_text:
            key, value = item.split(": ")
            f_output_graph[key] = value.split()


        f_graph = DeBruijnKmers(kmers)
        if f_output_graph == f_graph:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(f_graph, "\n", f_output_graph)

    file_input = open("/home/swativ5/Downloads/dataset_30184_8-4.txt")
    file_input_text = file_input.read().strip()
    kmers = file_input_text.split()
    graph = DeBruijnKmers(kmers)
    f = open("test.txt", "w")
    for key, value in sorted(graph.items()):
        f.write(f"{key}: {' '.join(sorted(value))}\n")
