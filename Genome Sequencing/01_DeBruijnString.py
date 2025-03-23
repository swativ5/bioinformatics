"""
Code Challenge: Solve the De Bruijn Graph from a String Problem.

    Input: An integer k and a string Text.
    Output: DeBruijnk(Text), in the form of an adjacency list.

Sample Input:
4
AAGATTCTCTAAGA

Sample Output:
AAG: AGA AGA
AGA: GAT
ATT: TTC
CTA: TAA
CTC: TCT
GAT: ATT
TAA: AAG
TCT: CTA CTC
TTC: TCT

"""

def KmerComposition(k, Text):
    kmers = set()
    kmers_list = []
    for i in range(len(Text) - k + 1):
        kmers.add(Text[i:i + k])
        kmers_list.append(Text[i:i + k])
    return kmers, kmers_list

def prefix(text):
    return text[:-1]

def suffix(text):
    return text[1:]

def DeBruijnString(k, Text):
    kmers = KmerComposition(k, Text)[1]
    graph = {}
    for kmer in kmers:
        graph[prefix(kmer)] = graph.get(prefix(kmer), []) + [suffix(kmer)]
    return graph

def parsing(text):
    k, Text = text.split('\n')
    return int(k), Text

if __name__ == "__main__":
    for i in range(5):
        file_input = open(f"DeBruijnString/inputs/input_{i + 1}.txt")
        file_input_text = file_input.read()
        k, Text = parsing(file_input_text)

        file_output = open(f"DeBruijnString/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip().split("\n")
        f_output_graph = {}
        for item in file_output_text:
            key, value = item.split(": ")
            f_output_graph[key] = value.split()


        f_graph = DeBruijnString(k, Text)
        if f_output_graph == f_graph:
            print(f"Test {i + 1} is Passed")
        else:
            print(f"Test {i + 1} is Failed")
            print(f_graph, "\n", f_output_graph)
    file_input = open("/home/swativ5/Downloads/dataset_30183_6.txt")
    file_input_text = file_input.read().strip()
    k, Text = parsing(file_input_text)
    graph = DeBruijnString(k, Text)
    f = open("test.txt", "w")
    for key, value in graph.items():
        f.write(f"{key}: {' '.join(value)} \n")
