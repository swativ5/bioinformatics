"""
Contig Generation Problem: Generate the contigs from a collection of reads (with imperfect coverage).
    Input: A collection of k-mers Patterns.
    Output: All contigs in DeBruijn(Patterns).

Sample Input:
ATG ATG TGT TGG CAT GGA GAT AGA

Sample Output:
AGA ATG ATG CAT GAT TGGA TGT
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
    return Paths

def ContigGeneration(kmers):
    graph = DeBruijnKmers(kmers)
    paths = MaximalNonBranchingPaths(graph)
    contigs = []
    for p in paths:
        contig = p[0] + ''.join(node[-1] for node in p[1:])
        contigs.append(contig)
    return contigs


def parsing(text):
    kmers = text.strip().split()
    return kmers

if __name__ == "__main__":
    for i in range(5):
        file_input = open(f"ContigGeneration/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        kmers = parsing(file_input_text)

        file_output = open(f"ContigGeneration/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        f_output = ContigGeneration(kmers)
        f_output = " ".join(f_output)

        if file_output_text == f_output:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(file_output_text, "\n", f_output)

    file_input = open(f"/home/swativ5/Downloads/dataset_30189_5.txt")
    file_input_text = file_input.read()
    kmers = parsing(file_input_text)
    f_output = ContigGeneration(kmers)
    f = open("test.txt", "w")
    f.write(" ".join(f_output))
