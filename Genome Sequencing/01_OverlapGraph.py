"""
Code Challenge: Solve the Overlap Graph Problem (restated below).
    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)

Note: You don't need to account for repeated elements in Patterns in this problem.

Sample Input:
ATGCG GCATG CATGC AGGCA GGCAT GGCAC

Sample Output:
CATGC: ATGCG
GCATG: CATGC
GGCAT: GCATG
AGGCA: GGCAC GGCAT

"""

def prefix(text):
    return text[:-1]

def suffix(text):
    return text[1:]

def OverlapGraph(kmers):
    graph = {}
    for kmer in kmers:
        graph[kmer] = []
    remove = []
    for kmer in graph.keys():
        for kmer2 in graph.keys():
            if suffix(kmer) == prefix(kmer2):
                graph[kmer].append(kmer2)
        if graph[kmer] == []:
            remove.append(kmer)
    for item in remove:
        del graph[item]
    return graph

if __name__ == "__main__":
    for i in range(4):
        file_input = open(f"OverlapGraph/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        kmers = file_input_text[0].strip().split()

        file_output = open(f"OverlapGraph/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip().split("\n")
        f_output_graph = {}
        for item in file_output_text:
            key, value = item.split(": ")
            f_output_graph[key] = value.split()


        f_graph = OverlapGraph(kmers)
        if f_output_graph == f_graph:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(f_graph, "\n", f_output_graph)

    file_input = open(f"/home/swativ5/Downloads/dataset_30182_10-1.txt")
    file_input_text = file_input.readlines()
    kmers = file_input_text[0].strip().split()
    graph = OverlapGraph(kmers)
    f = open("test.txt", "w")
    for key, value in graph.items():
        f.write(f"{key}: {' '.join(value)} \n")
