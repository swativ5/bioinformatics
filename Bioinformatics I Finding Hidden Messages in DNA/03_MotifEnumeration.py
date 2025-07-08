'''
Implement MotifEnumeration (reproduced below).

Input: Integers k and d, followed by a space-separated collection of strings Dna.
Output: All (k, d)-motifs in Dna.
MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns
'''
def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighbors = set()
    suffix_neighbors = Neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if HammingDistance(pattern[1:], text) < d:
            for nucleotide in 'ACGT':
                neighbors.add(nucleotide + text)
        else:
            neighbors.add(pattern[0] + text)
    return neighbors

def MotifEnumeration(Dna, k, d):
    Patterns = set()
    for sequence in Dna:  # loop over each DNA string in Dna
        for i in range(len(sequence) - k + 1):  # loop over each k-mer in the sequence
            pattern = sequence[i:i + k]
            for patternn in Neighbors(pattern, d):  # patternn in neighbors with at most d mismatches
                # Check if the patternn appears in all Dna with at most d mismatches
                if all(any(HammingDistance(patternn, other[i:i + k]) <= d for i in range(len(other) - k + 1)) for other in Dna):
                    Patterns.add(patternn)
    if len(Patterns) == 0:
        return {'nan'}
    return Patterns

if __name__ == '__main__':
    for i in range(6):
        file_input = open(f"MotifEnumeration/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        k, d = file_input_text[0].strip().split()
        DNA = file_input_text[1].strip().split()

        file_output = open(f"MotifEnumeration/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip().split()

        if set(file_output_text) == MotifEnumeration(DNA, int(k), int(d)):
            print("yes")
        else:
            print("no", file_input_text, MotifEnumeration(DNA, int(k), int(d)), file_output_text)

    k, d = 5, 2
    dna = "CGCTTGCACGTACTCAGATGTAGAT ATTGTAGAAGTCAAGGGCGGTTCCC TAATCTGATGCAAGCAGGTGCTCTT GTATGCGGGATATGGAGGCGTGGAA CCAATAGATGCGTCAAATTTCAGTT TAGGAACTCAAACGTCCCACAGTGG"
    DNA = dna.split()
    print(" ".join(map(str, MotifEnumeration(DNA, k, d))))
