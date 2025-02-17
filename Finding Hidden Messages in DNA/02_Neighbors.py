'''
Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

Input: A string Pattern and an integer d.
Output: The collection of strings Neighbors(Pattern, d). (You may return the strings in any order, but each line should contain only one string.)

ImmediateNeighbors(Pattern)
    Neighborhood ← the set consisting of single string Pattern
    for i = 1 to |Pattern|
        symbol ← i-th nucleotide of Pattern
        for each nucleotide x different from symbol
            Neighbor ← Pattern with the i-th nucleotide substituted by x
            add Neighbor to Neighborhood
    return Neighborhood

Neighbors(Pattern, d)
    if d = 0
        return {Pattern}
    if |Pattern| = 1 
        return {A, C, G, T}
    Neighborhood ← an empty set
    SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
    for each string Text from SuffixNeighbors
        if HammingDistance(Suffix(Pattern), Text) < d
            for each nucleotide x
                add x • Text to Neighborhood
        else
            add FirstSymbol(Pattern) • Text to Neighborhood
    return Neighborhood

IterativeNeighbors(Pattern, d)
    Neighborhood ← set consisting of single string Pattern
    for j = 1 to d
        for each string Pattern’ in Neighborhood
            add ImmediateNeighbors(Pattern') to Neighborhood
            remove duplicates from Neighborhood
    return Neighborhood
'''

def ImmediateNeighbors(Pattern):
    Neighborhood = set()
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for nucleotide in ['A', 'C', 'G', 'T']:
            Neighbor = Pattern[:i] + nucleotide + Pattern[i+1:]
            Neighborhood.add(Neighbor)
    Neighborhood.add(Pattern)
    return Neighborhood

def Neighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighbborhood = set()
    sneighbors = Neighbors(Pattern[1:], d)
    for text in sneighbors:
        if HammingDistance(Pattern[1:], text) < d:
            for x in ['A', 'C', 'G', 'T']:
                neighbborhood.add(x + text)
        else:
            neighbborhood.add(Pattern[0] + text)
    return neighbborhood

def IterativeNeighbors(Pattern, d):
    if d == 0:
        return {Pattern}
    Neighborhood = ImmediateNeighbors(Pattern)
    for j in range(1, d):
        for pattern in Neighborhood:
            Neighborhood.update(ImmediateNeighbors(pattern))
    return Neighborhood

def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

if __name__ == "__main__":
    print("Iterative Approach")
    for i in range(4):
        file_input = open(f"Neighborhood/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        Pattern = file_input_text[0].strip()
        d = int(file_input_text[1].strip())

        file_output = open(f"Neighborhood/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if set(file_output_text.split()) == IterativeNeighbors(Pattern, d):
            print("yes")
        else:
            print("no", file_input_text, IterativeNeighbors(Pattern, d), file_output_text)

    print("Recursive Approach")
    for i in range(4):
        file_input = open(f"Neighborhood/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        Pattern = file_input_text[0].strip()
        d = int(file_input_text[1].strip())

        file_output = open(f"Neighborhood/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if set(file_output_text.split()) == Neighbors(Pattern, d):
            print("yes")
        else:
            print("no", file_input_text, Neighbors(Pattern, d), file_output_text)