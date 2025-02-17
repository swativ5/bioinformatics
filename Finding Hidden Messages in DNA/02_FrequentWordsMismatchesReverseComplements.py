'''
Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a string.

Input: A DNA string Text as well as integers k and d.
Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc) over all possible k-mers.
Code Challenge: Solve the Frequent Words with Mismatches and Reverse Complements Problem.

def FrequentWordsWMARC(text, k, d):
    #Frequent Words with Mismatches and Reverse Complements
    counts = dict()
    for i in range(len(text)-k+1):
        neighbor = Neighbors(text[i:i+k], d)
        for n in neighbor:
            nrc = ReverseComplement(n)
            counts[n] = counts.get(n, 0) + 1
            counts[nrc] = counts.get(nrc, 0) + 1
    m = max(counts.values())
    return [t for t, v in counts.items() if v == m]      
'''

def HammingDistance(string1, string2):
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

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

def ReverseComplement(Pattern):
    Compliment = {"A":"T", "T":"A", "C":"G", "G":"C"};
    complement_list = [Compliment[c] for c in Pattern]
    reversed_compliment = "".join(complement_list[::-1])
    return reversed_compliment    

def FrequentWordsMismatchesReverseComplements(Text, k, d):
    Patterns = []
    freqMap = dict()
    n = len(Text)
    for i in range(n - k + 1):
        Pattern = Text[i:i+k]
        neighborhood = Neighbors(Pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood.pop()
            rneighbor = ReverseComplement(neighbor)
            freqMap[neighbor] = freqMap.get(neighbor, 0) + 1
            freqMap[rneighbor] = freqMap.get(rneighbor, 0) + 1
    m = max(freqMap.values())
    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)
    return Patterns

def MinimumSkew(genome):
    skew = [0]
    min_skew = 0
    for i in range(len(genome)):
        if genome[i] == "C":
            skew.append(skew[i] - 1)
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
        if skew[i+1] < min_skew:
            min_skew = skew[i+1]
    return [i for i, x in enumerate(skew) if x == min_skew]


if __name__ == "__main__":
    for i in range(5):
        file_input = open(f"FrequentWordsMismatchesReverseComplements/inputs/input_{i + 1}.txt")
        file_input_text = file_input.readlines()
        text = file_input_text[0].strip()
        k, d = map(int, file_input_text[1].strip().split())

        file_output = open(f"FrequentWordsMismatchesReverseComplements/outputs/output_{i + 1}.txt")
        file_output_text = file_output.read().strip()

        if set(file_output_text.split()) == set(FrequentWordsMismatchesReverseComplements(text, k, d)):
            print("yes")
        else:
            print(f"{i+1} no {FrequentWordsMismatchesReverseComplements(text, k, d)}, {file_output_text}")
    
    text = "TTTTTTTCTCGTTCTCGTTCGCTTCTTTTTTTTTGTACTTTACGTTTTTTTTCGTGCTTCGCTACTCGTGTTCGCTGTTTTTCGTGCTGCTTCACGCTGCTACTTTGCTGCTTCTCGTACGTTTTGTACTTTGCTACACTTTGTACTTTTTTGCTTCGCTACTTTACACGTACTCTTTTCGTTTTTTTGCTGTTCTTTGCT"
    k, d = 5, 3
    print(" ".join(map(str, FrequentWordsMismatchesReverseComplements(text, k, d))))
    
    
    f = open("Salmonella_enterica.txt")
    Genome = "".join(f.read().split("\n"))
    minSkews = MinimumSkew(Genome)
    k, d = 9, 1
    for minSkew in minSkews:
        genomeTextWindow = Genome[minSkew - 500:minSkew + 500]
        if len(genomeTextWindow) < 1000:
            genomeTextWindow = Genome[minSkew - 500:]
        if len(genomeTextWindow) < 1000:
            genomeTextWindow = Genome[:minSkew + 500]
        print(" ".join(map(str, FrequentWordsMismatchesReverseComplements(genomeTextWindow, k, d))))