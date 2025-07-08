'''
Implement MedianString.

Input: An integer k, followed by a space-separated collection of strings Dna.
Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. 
(If there are multiple such strings Pattern, then you may return any one.)

MedianString(Dna, k)
    distance ← ∞
    for each k-mer Pattern from AA…AA to TT…TT
        if distance > d(Pattern, Dna)
             distance ← d(Pattern, Dna)
             Median ← Pattern
    return Median

DistanceBetweenPatternAndStrings(Pattern, Dna)
    k ← |Pattern|
    distance ← 0
    for each string Text in Dna
        HammingDistance ← ∞
        for each k-mer Pattern’ in Text
            if HammingDistance > HammingDistance(Pattern, Pattern’)
                HammingDistance ← HammingDistance(Pattern, Pattern’)
        distance ← distance + HammingDistance
    return distance
'''

def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        hammingDistance = float('inf')
        for i in range(len(Text) - k + 1):
            Pattern_ = Text[i:i + k]
            if hammingDistance > HammingDistance(Pattern, Pattern_):
                hammingDistance = HammingDistance(Pattern, Pattern_)
        distance += hammingDistance
    return distance

def MedianString(Dna, k):
    distance = float('inf')
    for Pattern in GeneratePatterns(k):
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    return Median

def GeneratePatterns(k):
    if k == 1:
        return ['A', 'C', 'G', 'T']
    Patterns = []
    nucleotides = ['A', 'C', 'G', 'T']
    while len(Patterns) < 4 ** k:
        if len(Patterns) == 0:
            Patterns = GeneratePatterns(k - 1)
        else:
            Patterns = [Pattern + nucleotide for Pattern in Patterns for nucleotide in nucleotides]
    return Patterns

if __name__ == "__main__":
    for i in range(4):
        file_input = open(f"MedianString/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        k = int(file_input_text[0].strip())
        Dna = file_input_text[1].strip().split()

        file_output = open(f"MedianString/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if file_output_text == MedianString(Dna, k):
            print("yes")
        else:
            print("no", file_input_text, MedianString(Dna, k), file_output_text)

    k = 6
    Dna = """GGGTAAAATAATCCAAACGGCTCAATCAGCGAGTGCGCCGGT
CTTATGACAAACACTTTGACTAAAATAGACCCTCACTCCGAG
ACGCTATCAAACATTGTGACTCGCTCGGGTTCACCATGCAAG
TGCGAACCCTTTTCTATACCAAACGTATCACAATTTCGAAAG
CAAGTGGCGAACGAACCCGATTTAAGGTTGCCAAACAGCGGA
GCAGCGTACTAACCCCTACTAGCCGGCAGGCCCGTCCCAAAC
CCCCGCAGATGCTGGCTCTAATCTGCAAACCTAGGACCACCC
TGTATAGTATCCAAACCGTCAGCCTCAAACTACCCTGCGAAT
TCCGAGTCAAACTACATGTATACGGGTCCGTCCAGATTTCTA
CCGCTCTCTAACCCCTTTCGTAAGCTAAGCCACGTCCCAAAC"""
    Dna = Dna.split()
    print(MedianString(Dna, k))