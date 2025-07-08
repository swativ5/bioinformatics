'''
def FrequentWordsWithMismatches(text, k, d):
    counts = dict()
    for i in range(len(text)-k+1):
        neighbor = Neighbors(text[i:i+k], d)
        for n in neighbor:
            counts[n] = counts.get(n, 0) + 1
    m = max(counts.values())
    return [t for t, v in counts.items() if v == m]  

FrequentWordsWithMismatches(Text, k, d)
    Patterns ← an array of strings of length 0
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n - k
        Pattern ← Text(i, k)
        neighborhood ← Neighbors(Pattern, d)
        for j ← 0 to |neighborhood| - 1
            neighbor ← neighborhood[j]
            if freqMap[neighbor] doesn't exist
                freqMap[neighbor] ← 1
            else
                freqMap[neighbor] ← freqMap[neighbor] + 1
    m ← MaxMap(freqMap)
    for every key Pattern in freqMap
        if freqMap[Pattern] = m
            append Pattern to Patterns
    return Patterns

Code Challenge: Solve the Frequent Words with Mismatches Problem.

Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
Output: All most frequent k-mers with up to d mismatches in Text.

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
'''

# def ImmediateNeighbors(Pattern):
#     neighborhood = set()
#     for i in range(len(Pattern)):
#         for x in ['A', 'C', 'G', 'T']:
#             neighbor = Pattern[:i] + x + Pattern[i+1:]
#             neighborhood.add(neighbor)
#     neighborhood.add(Pattern)
#     return neighborhood


def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

def Neighbors(Pattern, d):
    # recursive approach
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


def FrequentWordsMismatches(Text, k, d):
    Patterns = []
    freqMap = dict()
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i+k]
        neighborhood = Neighbors(Pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood.pop()
            freqMap[neighbor] = freqMap.get(neighbor, 0) + 1
    m = max(freqMap.values())
    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)
    return Patterns

if __name__ == '__main__':
    for i in range(4):
        file_input = open(f"FrequentWordsMismatches/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        Text = file_input_text[0].strip()
        k, d = map(int, file_input_text[1].strip().split())

        file_output = open(f"FrequentWordsMismatches/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if set(file_output_text.split()) == set(FrequentWordsMismatches(Text, k, d)):
            print("yes")
        else:
            print(f"{i+1} no {FrequentWordsMismatches(Text, k, d)}, {file_output_text}")

    # Text = "CGGCGAAGTATATGATGATGATGACACGGGTATGTATACAACAACAACAGTATCGGCGAAGTATACAGTATACACGGCGGATGCGAAACAATGGTATCGGCGAACGGGTATCGAAATGCGAACGAACGGACAACAATGATGACACGAACGAAGTATCGGCGGCGGCGAACGAAGTATACAACACGAACGGATGACAATGACACGAAACAATGCGGGTATCGGCGAAGTATCGAACGAAGTATCGAAGTATACAGTATACAGTATATGACACGGATGCGAAACAGTATCGAACGAAGTATGTATCGGATGCGGATGCGAAATGACACGAAGTATCGAACGGATGATGGTAT"
    # k, d = 5, 2
    # print(FrequentWordsMismatches(Text, k, d))

    Text = "ACGT"
    d = 3
    k = 4
    print(len(FrequentWordsMismatches(Text, k, d)))